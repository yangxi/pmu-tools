#!/usr/bin/python
# Import perf.data into a pandas DataFrame
import pandas as pd
import numpy as np
import perfdata
from collections import defaultdict, Counter
import bisect
import elf
import mmap

#
# TBD 
# fix all types?
# extra table for threads?
# stream_id
# flatten callchains and branch_stack
# expand registers, stack
# represent other metadata
# s/w trace points
# debuginfo / buildid
# instructions / basic blocks
# 

ignored = {'type', 'start', 'end', '__recursion_lock__', 'ext_reserved',
           'header_end', 'end_event', 'offset', 'callchain', 'branch',
           'branch_stack', 'end_id', 'size',
           # skip attr for now, as it is too complex
           # XXX simple representation
           'attr'}

def resolve_list(j, ip, mm, need_line):
     filename, _, foffset = mm.resolve(j.pid, ip)
     sym, soffset, line = elf.resolve_ip(filename, foffset, ip, need_line)
     return [filename, sym, soffset, line]

def resolve_chain(cc, j, mm, need_line):
    if not cc:
        return []
    res = []
    for ip in cc.caller:
        r = [ip,]
        r += resolve_list(j, ip, mm, need_line)
        res.append(r)
    return res

def resolve_branch(branch, j, mm, need_line):
    res = []
    for br in branch:
        # XXX flags
        r = [br['from'], br['to']]
        r += resolve_list(j, br['from'], mm, need_line)
        r += resolve_list(j, br['to'], mm, need_line)
        res.append(r)
    return res

class Path:
    pass

class Aux:
    """Store auxilliary data to the main pandas perf array, like call chains
       or branch stacks. The data is deduped and a unique id generated."""

    def __init__(self):
        self.ids = dict()
        self.paths = dict()
        self.next_id = 0

    def alloc_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def add(self, h, create):
        h = tuple(h)
        if h in self.paths:
            return self.paths[h].id
        id = self.alloc_id()
        path = Path()
        path.val = create()
        path.id = id
        self.paths[h] = path
        self.ids[id] = path
        return id

    def getid(self, id):
        return self.ids[id]

def do_add(d, u, k, i):
    d[k].append(i)
    u[k] += 1

def samples_to_df(h, need_line):
    """Convert a parsed perf event list to a pandas table.
       The pandas table contains all events in a easily to process format.
       The pandas table has callchain_aux and branch_aux fields pointing
       to Aux object defining the callchains/branches."""
    ev = perfdata.get_events(h)
    index = []
    data = defaultdict(list)
    callchains = Aux()
    branches = Aux()

    used = Counter()
    mm = mmap.MmapTracker()

    for n in range(0, len(ev)):
        mm.lookahead_mmap(ev, n)

        j = ev[n]
        if j.type != "SAMPLE":
            continue

        mm.update_sample(j)
        add = lambda k, i: do_add(data, used, k, i)

        filename, mmap_base, foffset = mm.resolve(j.pid, j.ip)
        add('filename', filename)
        add('foffset', foffset)
        sym, soffset, line = elf.resolve_ip(filename, foffset, j.ip, need_line)
        add('symbol', sym)
        add('line', line)
        add('soffset', soffset)
        if 'callchain' in j and j['callchain']:
            id = callchains.add(j['callchain'].caller,
                    lambda: resolve_chain(j['callchain'], j, mm, need_line))
            add('callchain', id)
        if 'branch' in j:
            id = branches.add(map(lambda x: (x['from'], x.to),  j['branch']),
                    lambda: resolve_branch(j['branch'], j, mm, need_line))
            add('branch', id)
        for name in j:
            if name not in ignored:
                if j[name]:
                    used[name] += 1
                data[name].append(j[name])
        index.append(int(j["time"]))
    for j in data.keys():
        if used[j] == 0:
            del data[j]
    df = pd.DataFrame(data, index=index, dtype=np.uint64)
    df.branch_aux = branches
    df.callchain_aux = callchains
    return df

def read_samples(fn, need_line=True):
    with open(fn, "rb") as f:
        h = perfdata.perf_file.parse_stream(f)
        df = samples_to_df(h, need_line)
        return df, h.attrs.perf_file_attr.f_attr, h.features

if __name__ == '__main__':
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument('file', nargs='?', help='perf.data file to read', 
                          default='perf.data')
    args.add_argument('--repl', action='store_true',
                             help='start python shell with data')
    p = args.parse_args()
    df, _, _ = read_samples(p.file)
    if p.repl:
        import code
        print df
        code.interact(banner='perf.data is in df', local=locals())
        sys.exit(0)

    print df
    print df['filename'].value_counts()
    print df['symbol'].value_counts()
    print df['line'].value_counts()
