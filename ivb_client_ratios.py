
#
# auto generated TopDown/TMAM 3.1 description for Intel 3rd gen Core (code named IvyBridge)
# Please see http://ark.intel.com for more details on these CPUs.
#
# References:
# http://halobates.de/blog/p/262
# https://sites.google.com/site/analysismethods/yasin-pubs
# https://download.01.org/perfmon/
#

# Helpers

print_error = lambda msg: False
smt_enabled = False
version = "3.1"



# Constants

Pipeline_Width = 4
Mem_L2_Store_Cost = 9
Mem_L3_Weight = 7
Mem_STLB_Hit_Cost = 7
Mem_4K_Alias_Cost = 7
Mem_XSNP_HitM_Cost = 60
MEM_XSNP_Hit_Cost = 43
MEM_XSNP_None_Cost = 29
MS_Switches_Cost = 3
OneMillion = 1000000
OneBillion = 1000000000
Energy_Unit = 15.6

# Aux. formulas


# Floating Point computational (arithmetic) Operations Count
def FLOP_Count(self, EV, level):
    return (1 *(EV("FP_COMP_OPS_EXE.SSE_SCALAR_SINGLE", level) + EV("FP_COMP_OPS_EXE.SSE_SCALAR_DOUBLE", level)) + 2 * EV("FP_COMP_OPS_EXE.SSE_PACKED_DOUBLE", level) + 4 *(EV("FP_COMP_OPS_EXE.SSE_PACKED_SINGLE", level) + EV("SIMD_FP_256.PACKED_DOUBLE", level)) + 8 * EV("SIMD_FP_256.PACKED_SINGLE", level))

def Recovery_Cycles(self, EV, level):
    return (EV("INT_MISC.RECOVERY_CYCLES_ANY", level) / 2) if smt_enabled else EV("INT_MISC.RECOVERY_CYCLES", level)

def Execute_Cycles(self, EV, level):
    return (EV("UOPS_EXECUTED.CORE:c1", level) / 2) if smt_enabled else EV("UOPS_EXECUTED.CYCLES_GE_1_UOP_EXEC", level)

def L1D_Miss_Cycles(self, EV, level):
    return (EV("L1D_PEND_MISS.PENDING_CYCLES:amt1", level) / 2) if smt_enabled else EV("L1D_PEND_MISS.PENDING_CYCLES", level)

def SQ_Full_Cycles(self, EV, level):
    return (EV("OFFCORE_REQUESTS_BUFFER.SQ_FULL", level) / 2) if smt_enabled else EV("OFFCORE_REQUESTS_BUFFER.SQ_FULL", level)

def ITLB_Miss_Cycles(self, EV, level):
    return (Mem_STLB_Hit_Cost * EV("ITLB_MISSES.STLB_HIT", level) + EV("ITLB_MISSES.WALK_DURATION", level))

def Frontend_RS_Empty_Cycles(self, EV, level):
    EV("RS_EVENTS.EMPTY_CYCLES", level)
    return EV("RS_EVENTS.EMPTY_CYCLES", level) if(self.Frontend_Latency.compute(EV)> 0.1)else 0

def Cycles_0_Ports_Utilized(self, EV, level):
    return (EV("UOPS_EXECUTED.CORE:i1:c1", level)) / 2 if smt_enabled else(STALLS_TOTAL(self, EV, level) - Frontend_RS_Empty_Cycles(self, EV, level))

def Cycles_1_Port_Utilized(self, EV, level):
    return (EV("UOPS_EXECUTED.CORE:c1", level) - EV("UOPS_EXECUTED.CORE:c2", level)) / 2 if smt_enabled else(EV("UOPS_EXECUTED.CYCLES_GE_1_UOP_EXEC", level) - EV("UOPS_EXECUTED.CYCLES_GE_2_UOPS_EXEC", level))

def Cycles_2_Ports_Utilized(self, EV, level):
    return (EV("UOPS_EXECUTED.CORE:c2", level) - EV("UOPS_EXECUTED.CORE:c3", level)) / 2 if smt_enabled else(EV("UOPS_EXECUTED.CYCLES_GE_2_UOPS_EXEC", level) - EV("UOPS_EXECUTED.CYCLES_GE_3_UOPS_EXEC", level))

def Cycles_3m_Ports_Utilized(self, EV, level):
    return (EV("UOPS_EXECUTED.CORE:c3", level) / 2) if smt_enabled else EV("UOPS_EXECUTED.CYCLES_GE_3_UOPS_EXEC", level)

def Frontend_Latency_Cycles(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("IDQ_UOPS_NOT_DELIVERED.CYCLES_0_UOPS_DELIV.CORE", level)) , level )

def STALLS_MEM_ANY(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("CYCLE_ACTIVITY.STALLS_LDM_PENDING", level)) , level )

def STALLS_TOTAL(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("CYCLE_ACTIVITY.CYCLES_NO_EXECUTE", level)) , level )

def ORO_DRD_Any_Cycles(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("OFFCORE_REQUESTS_OUTSTANDING.CYCLES_WITH_DATA_RD", level)) , level )

def ORO_DRD_BW_Cycles(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("OFFCORE_REQUESTS_OUTSTANDING.ALL_DATA_RD:c6", level)) , level )

def ORO_Demand_RFO_C1(self, EV, level):
    return EV(lambda EV , level : min(EV("CPU_CLK_UNHALTED.THREAD", level) , EV("OFFCORE_REQUESTS_OUTSTANDING.CYCLES_WITH_DEMAND_RFO", level)) , level )

def Store_L2_Hit_Cycles(self, EV, level):
    return 0

def LOAD_L1_MISS_CLT(self, EV, level):
    return EV("MEM_LOAD_UOPS_RETIRED.L2_HIT", level) + EV("MEM_LOAD_UOPS_RETIRED.LLC_HIT", level) + EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HIT", level) + EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HITM", level) + EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_MISS", level)

def LOAD_L1_MISS_NET(self, EV, level):
    return LOAD_L1_MISS_CLT(self, EV, level)

def LOAD_L3_HIT(self, EV, level):
    return EV("MEM_LOAD_UOPS_RETIRED.LLC_HIT", level)*(1 + EV("MEM_LOAD_UOPS_RETIRED.HIT_LFB", level) / LOAD_L1_MISS_NET(self, EV, level))

def LOAD_XSNP_HIT(self, EV, level):
    return EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HIT", level)*(1 + EV("MEM_LOAD_UOPS_RETIRED.HIT_LFB", level) / LOAD_L1_MISS_NET(self, EV, level))

def LOAD_XSNP_HITM(self, EV, level):
    return EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HITM", level)*(1 + EV("MEM_LOAD_UOPS_RETIRED.HIT_LFB", level) / LOAD_L1_MISS_NET(self, EV, level))

def LOAD_XSNP_MISS(self, EV, level):
    return EV("MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_MISS", level)*(1 + EV("MEM_LOAD_UOPS_RETIRED.HIT_LFB", level) / LOAD_L1_MISS_NET(self, EV, level))

def Few_Uops_Executed_Threshold(self, EV, level):
    EV("UOPS_EXECUTED.CYCLES_GE_3_UOPS_EXEC", level)
    EV("UOPS_EXECUTED.CYCLES_GE_2_UOPS_EXEC", level)
    return EV("UOPS_EXECUTED.CYCLES_GE_3_UOPS_EXEC", level) if(IPC(self, EV, level)> 1.8)else EV("UOPS_EXECUTED.CYCLES_GE_2_UOPS_EXEC", level)

def Backend_Bound_Cycles(self, EV, level):
    return (STALLS_TOTAL(self, EV, level) + EV("UOPS_EXECUTED.CYCLES_GE_1_UOP_EXEC", level) - Few_Uops_Executed_Threshold(self, EV, level) - Frontend_RS_Empty_Cycles(self, EV, level) + EV("RESOURCE_STALLS.SB", level))

def Memory_Bound_Fraction(self, EV, level):
    return (STALLS_MEM_ANY(self, EV, level) + EV("RESOURCE_STALLS.SB", level)) / Backend_Bound_Cycles(self, EV, level)

def Mem_L3_Hit_Fraction(self, EV, level):
    return EV("MEM_LOAD_UOPS_RETIRED.LLC_HIT", level) /(EV("MEM_LOAD_UOPS_RETIRED.LLC_HIT", level) + Mem_L3_Weight * EV("MEM_LOAD_UOPS_RETIRED.LLC_MISS", level))

def Mem_Lock_St_Fraction(self, EV, level):
    return EV("MEM_UOPS_RETIRED.LOCK_LOADS", level) / EV("MEM_UOPS_RETIRED.ALL_STORES", level)

def Mispred_Clears_Fraction(self, EV, level):
    return EV("BR_MISP_RETIRED.ALL_BRANCHES", level) /(EV("BR_MISP_RETIRED.ALL_BRANCHES", level) + EV("MACHINE_CLEARS.COUNT", level))

def Avg_RS_Empty_Period_Clears(self, EV, level):
    return (EV("RS_EVENTS.EMPTY_CYCLES", level) - EV("ICACHE.IFETCH_STALL", level)) / EV("RS_EVENTS.EMPTY_END", level)

def Retire_Uop_Fraction(self, EV, level):
    return EV("UOPS_RETIRED.RETIRE_SLOTS", level) / EV("UOPS_ISSUED.ANY", level)

def DurationTimeInSeconds(self, EV, level):
    return 0 if 0 > 0 else(EV("interval-ns", 0) / 1e+06 / 1000 )

def r2r_delta(self, EV, level):
    return max_delta_clk

# Instructions Per Cycle (per logical thread)
def IPC(self, EV, level):
    return EV("INST_RETIRED.ANY", level) / CLKS(self, EV, level)

# Uops Per Instruction
def UPI(self, EV, level):
    return EV("UOPS_RETIRED.RETIRE_SLOTS", level) / EV("INST_RETIRED.ANY", level)

# Instruction per taken branch
def IPTB(self, EV, level):
    return EV("INST_RETIRED.ANY", level) / EV("BR_INST_RETIRED.NEAR_TAKEN", level)

# Branch instructions per taken branch. Can be used to approximate PGO-likelihood for non-loopy codes.
def BPTB(self, EV, level):
    return EV("BR_INST_RETIRED.ALL_BRANCHES", level) / EV("BR_INST_RETIRED.NEAR_TAKEN", level)

# Rough Estimation of fraction of fetched lines bytes that were likely consumed by program instructions
def IFetch_Line_Utilization(self, EV, level):
    return min(1 , EV("UOPS_ISSUED.ANY", level) /(UPI(self, EV, level)* 32 *(EV("ICACHE.HIT", level) + EV("ICACHE.MISSES", level)) / 4))

# Fraction of Uops delivered by the DSB (decoded instructions cache)
def DSB_Coverage(self, EV, level):
    return (EV("IDQ.DSB_UOPS", level) + EV("LSD.UOPS", level)) /(EV("IDQ.DSB_UOPS", level) + EV("LSD.UOPS", level) + EV("IDQ.MITE_UOPS", level) + EV("IDQ.MS_UOPS", level))

# Cycles Per Instruction (threaded)
def CPI(self, EV, level):
    return 1 / IPC(self, EV, level)

# Per-thread actual clocks when the thread is active
def CLKS(self, EV, level):
    return EV("CPU_CLK_UNHALTED.THREAD", level)

# Total issue-pipeline slots
def SLOTS(self, EV, level):
    return Pipeline_Width * CORE_CLKS(self, EV, level)

# Instructions Per Cycle (per physical core)
def CoreIPC(self, EV, level):
    return EV("INST_RETIRED.ANY", level) / CORE_CLKS(self, EV, level)

# Floating Point Operations Per Cycle
def FLOPc(self, EV, level):
    return FLOP_Count(self, EV, level) / CORE_CLKS(self, EV, level)

# Instruction-Level-Parallelism (average number of uops executed when there is at least 1 uop executed)
def ILP(self, EV, level):
    return EV("UOPS_EXECUTED.THREAD", level) / Execute_Cycles(self, EV, level)

# Memory-Level-Parallelism (average number of L1 miss demand load when there is at least 1 such miss)
def MLP(self, EV, level):
    return EV("L1D_PEND_MISS.PENDING", level) / L1D_Miss_Cycles(self, EV, level)

# Utilization of the core's Page Walker(s) serving STLB misses triggered by instruction/Load/Store accesses
def Page_Walks_Use(self, EV, level):
    return (EV("ITLB_MISSES.WALK_DURATION", level) + EV("DTLB_LOAD_MISSES.WALK_DURATION", level) + EV("DTLB_STORE_MISSES.WALK_DURATION", level)) / CORE_CLKS(self, EV, level)

# Core actual clocks when any thread is active on the physical core
def CORE_CLKS(self, EV, level):
    return (EV("CPU_CLK_UNHALTED.THREAD_ANY", level) / 2) if smt_enabled else CLKS(self, EV, level)

# Actual Average Latency for L1 data-cache miss demand loads
def Load_Miss_Real_Latency(self, EV, level):
    return EV("L1D_PEND_MISS.PENDING", level) /(EV("MEM_LOAD_UOPS_RETIRED.L1_MISS", level) + EV("MEM_LOAD_UOPS_RETIRED.HIT_LFB", level))

# Average CPU Utilization
def CPU_Utilization(self, EV, level):
    return EV("CPU_CLK_UNHALTED.REF_TSC", level) / EV("msr/tsc/", 0)

# Giga Floating Point Operations Per Second
def GFLOPs(self, EV, level):
    return FLOP_Count(self, EV, level) / OneBillion / DurationTimeInSeconds(self, EV, level)

# Average Frequency Utilization relative nominal frequency
def Turbo_Utilization(self, EV, level):
    return CLKS(self, EV, level) / EV("CPU_CLK_UNHALTED.REF_TSC", level)

# Fraction of cycles where both hardware threads were active
def SMT_2T_Utilization(self, EV, level):
    return 1 - EV("CPU_CLK_THREAD_UNHALTED.ONE_THREAD_ACTIVE", level) /(EV("CPU_CLK_THREAD_UNHALTED.REF_XCLK_ANY", level) / 2) if smt_enabled else 0

# Fraction of cycles spent in Kernel mode
def Kernel_Utilization(self, EV, level):
    return EV("CPU_CLK_UNHALTED.REF_TSC:sup", level) / EV("CPU_CLK_UNHALTED.REF_TSC", level)

# Average external Memory Bandwidth Use for reads and writes [GB / sec]
def MEM_BW_GBs(self, EV, level):
    return 64 *(EV("UNC_ARB_TRK_REQUESTS.ALL", level) + EV("UNC_ARB_COH_TRK_REQUESTS.ALL", level)) / OneMillion / DurationTimeInSeconds(self, EV, level) / 1000

# Average latency of all requests to external memory (in Uncore cycles)
def MEM_Request_Latency(self, EV, level):
    return EV("UNC_ARB_TRK_OCCUPANCY.ALL", level) / EV("UNC_ARB_TRK_REQUESTS.ALL", level)

# Average number of parallel requests to external memory (in Uncore cycles). Accounts for all requests
def MEM_Parallel_Requests(self, EV, level):
    return EV("UNC_ARB_TRK_OCCUPANCY.ALL", level) / EV("UNC_ARB_TRK_OCCUPANCY.CYCLES_WITH_ANY_REQUEST", level)

# Run duration time in seconds
def Time(self, EV, level):
    return DurationTimeInSeconds(self, EV, level)

def Socket_CLKS(self, EV, level):
    return EV("UNC_CLOCK.SOCKET", level)

# Event groups


class Frontend_Bound:
    name = "Frontend_Bound"
    domain = "Slots"
    area = "FE"
    desc = """
This category represents slots fraction where the
processor's Frontend undersupplies its Backend. Frontend
denotes the first part of the processor core responsible to
fetch operations that are executed later on by the Backend
part. Within the Frontend, a branch predictor predicts the
next address to fetch, cache-lines are fetched from the
memory subsystem, parsed into instructions, and lastly
decoded into micro-ops (uops). Ideally the Frontend can
issue 4 uops every cycle to the Backend. Frontend Bound
denotes unutilized issue-slots when there is no Backend
stall; i.e. bubbles where Frontend delivered no uops while
Backend could have accepted them. For example, stalls due to
instruction-cache misses would be categorized under Frontend
Bound."""
    level = 1
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("IDQ_UOPS_NOT_DELIVERED.CORE", 1) / SLOTS(self, EV, 1 )
            self.thresh = (self.val > 0.2)
        except ZeroDivisionError:
            print_error("Frontend_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Frontend_Latency:
    name = "Frontend_Latency"
    domain = "Slots"
    area = "FE"
    desc = """
This metric represents slots fraction the CPU was stalled
due to Frontend latency issues.  For example, instruction-
cache misses, iTLB misses or fetch stalls after a branch
misprediction are categorized under Frontend Latency. In
such cases, the Frontend eventually delivers no uops for
some period."""
    level = 2
    htoff = False
    sample = ['RS_EVENTS.EMPTY_END']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Pipeline_Width * Frontend_Latency_Cycles(self, EV, 2) / SLOTS(self, EV, 2 )
            self.thresh = (self.val > 0.15) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Frontend_Latency zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class ICache_Misses:
    name = "ICache_Misses"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric represents cycles fraction the CPU was stalled
due to instruction cache misses.. Using compiler's Profile-
Guided Optimization (PGO) can reduce i-cache misses through
improved hot code layout."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("ICACHE.IFETCH_STALL", 3) / CLKS(self, EV, 3) - self.ITLB_Misses.compute(EV )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("ICache_Misses zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class ITLB_Misses:
    name = "ITLB_Misses"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric represents cycles fraction the CPU was stalled
due to instruction TLB misses.. Using large code pages may
be considered here."""
    level = 3
    htoff = False
    sample = ['ITLB_MISSES.WALK_COMPLETED']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = ITLB_Miss_Cycles(self, EV, 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("ITLB_Misses zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Branch_Resteers:
    name = "Branch_Resteers"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric represents cycles fraction the CPU was stalled
due to Branch Resteers. Branch Resteers estimates the
Frontend delay in fetching operations from corrected path,
following all sorts of miss-predicted branches. For example,
branchy code with lots of miss-predictions might get
categorized under Branch Resteers. Note the value of this
node may overlap with its siblings."""
    level = 3
    htoff = False
    sample = ['BR_MISP_RETIRED.ALL_BRANCHES:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Avg_RS_Empty_Period_Clears(self, EV, 3)*(EV("BR_MISP_RETIRED.ALL_BRANCHES", 3) + EV("MACHINE_CLEARS.COUNT", 3) + EV("BACLEARS.ANY", 3)) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Branch_Resteers zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class DSB_Switches:
    name = "DSB_Switches"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric represents cycles fraction the CPU was stalled
due to switches from DSB to MITE pipelines. The DSB (decoded
i-cache, introduced with the Sandy Bridge microarchitecture)
pipeline has shorter latency and delivered higher bandwidth
than the MITE (legacy instruction decode pipeline).
Switching between the two pipelines can cause penalties.
This metric estimates when such penalty can be exposed.
Optimizing for better DSB hit rate may be considered.. See
section \"Optimization for Decoded ICache\" in Optimization
Guide:. http://www.intel.com/content/www/us/en/architecture-
and-technology/64-ia-32-architectures-optimization-
manual.html"""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("DSB2MITE_SWITCHES.PENALTY_CYCLES", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("DSB_Switches zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class LCP:
    name = "LCP"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric represents cycles fraction CPU was stalled due
to Length Changing Prefixes (LCPs). Using proper compiler
flags or Intel Compiler by default will certainly avoid
this."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("ILD_STALL.LCP", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("LCP zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class MS_Switches:
    name = "MS_Switches"
    domain = "Clocks"
    area = "FE"
    desc = """
This metric estimates the fraction of cycles when the CPU
was stalled due to switches of uop delivery to the Microcode
Sequencer (MS). Commonly used instructions are optimized for
delivery by the DSB or MITE pipelines. Certain operations
cannot be handled natively by the execution pipeline, and
must be performed by microcode (small programs injected into
the execution stream). Switching to the MS too often can
negatively impact performance. The MS is designated to
deliver long uop flows required by CISC instructions like
CPUID, or uncommon conditions like Floating Point Assists
when dealing with Denormals."""
    level = 3
    htoff = False
    sample = ['IDQ.MS_SWITCHES']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = MS_Switches_Cost * EV("IDQ.MS_SWITCHES", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("MS_Switches zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Frontend_Bandwidth:
    name = "Frontend_Bandwidth"
    domain = "Slots"
    area = "BAD"
    desc = """
This metric represents slots fraction the CPU was stalled
due to Frontend bandwidth issues.  For example,
inefficiencies at the instruction decoders, or code
restrictions for caching in the DSB (decoded uops cache) are
categorized under Frontend Bandwidth. In such cases, the
Frontend typically delivers non-optimal amount of uops to
the Backend (less than four)."""
    level = 2
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = self.Frontend_Bound.compute(EV) - self.Frontend_Latency.compute(EV )
            self.thresh = (self.val > 0.1) & (IPC(self, EV, 2) > 2.0) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Frontend_Bandwidth zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class MITE:
    name = "MITE"
    domain = "CoreClocks"
    area = "FE"
    desc = """
This metric represents Core cycles fraction in which CPU was
likely limited due to the MITE fetch pipeline (legacy non
cached decoding). This pipeline is used for code that was
not pre-cached in the DSB or LSD. For example,
inefficiencies in the instruction decoders are categorized
here."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = (EV("IDQ.ALL_MITE_CYCLES_ANY_UOPS", 3) - EV("IDQ.ALL_MITE_CYCLES_4_UOPS", 3)) / CORE_CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("MITE zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class DSB:
    name = "DSB"
    domain = "CoreClocks"
    area = "FE"
    desc = """
This metric represents Core cycles fraction in which CPU was
likely limited due to DSB (decoded uop cache) fetch
pipeline.  For example, inefficient utilization of the DSB
cache structure or bank conflict when reading from it, are
categorized here."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = (EV("IDQ.ALL_DSB_CYCLES_ANY_UOPS", 3) - EV("IDQ.ALL_DSB_CYCLES_4_UOPS", 3)) / CORE_CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.3) and self.parent.thresh
        except ZeroDivisionError:
            print_error("DSB zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class LSD:
    name = "LSD"
    domain = "CoreClocks"
    area = "FE"
    desc = """
This metric represents Core cycles fraction in which CPU was
likely limited due to LSD (Loop Stream Detector) unit.  LSD
typically does well sustaining Uop supply. However, in some
rare cases, optimal uop-delivery could not be reached for
small loops whose size (in terms of number of uops) does not
suit well the LSD structure."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = (EV("LSD.CYCLES_ACTIVE", 3) - EV("LSD.CYCLES_4_UOPS", 3)) / CORE_CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("LSD zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Bad_Speculation:
    name = "Bad_Speculation"
    domain = "Slots"
    area = "BAD"
    desc = """
This category represents slots fraction wasted due to
incorrect speculations. This include slots used to issue
uops that do not eventually get retired and slots for which
the issue-pipeline was blocked due to recovery from earlier
incorrect speculation. For example, wasted work due to miss-
predicted branches are categorized under Bad Speculation
category. Incorrect data speculation followed by Memory
Ordering Nukes is another example."""
    level = 1
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (EV("UOPS_ISSUED.ANY", 1) - EV("UOPS_RETIRED.RETIRE_SLOTS", 1) + Pipeline_Width * Recovery_Cycles(self, EV, 1)) / SLOTS(self, EV, 1 )
            self.thresh = (self.val > 0.1)
        except ZeroDivisionError:
            print_error("Bad_Speculation zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Branch_Mispredicts:
    name = "Branch_Mispredicts"
    domain = "Slots"
    area = "BAD"
    desc = """
This metric represents slots fraction the CPU has wasted due
to Branch Misprediction.  These slots are either wasted by
uops fetched from an incorrectly speculated program path, or
stalls when the out-of-order part of the machine needs to
recover its state from a speculative path.. Using profile
feedback in the compiler may help. Please see the
optimization manual for general strategies for addressing
branch misprediction issues..
http://www.intel.com/content/www/us/en/architecture-and-
technology/64-ia-32-architectures-optimization-manual.html"""
    level = 2
    htoff = False
    sample = ['BR_MISP_RETIRED.ALL_BRANCHES:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Mispred_Clears_Fraction(self, EV, 2)* self.Bad_Speculation.compute(EV )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Branch_Mispredicts zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Machine_Clears:
    name = "Machine_Clears"
    domain = "Slots"
    area = "BAD"
    desc = """
This metric represents slots fraction the CPU has wasted due
to Machine Clears.  These slots are either wasted by uops
fetched prior to the clear, or stalls the out-of-order
portion of the machine needs to recover its state after the
clear. For example, this can happen due to memory ordering
Nukes (e.g. Memory Disambiguation) or Self-Modifying-Code
(SMC) nukes.. See \"Memory Disambiguation\" in Optimization
Guide and:. https://software.intel.com/sites/default/files/m
/d/4/1/d/8/sma.pdf"""
    level = 2
    htoff = False
    sample = ['MACHINE_CLEARS.COUNT']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = self.Bad_Speculation.compute(EV) - self.Branch_Mispredicts.compute(EV )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Machine_Clears zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Backend_Bound:
    name = "Backend_Bound"
    domain = "Slots"
    area = "BE"
    desc = """
This category represents slots fraction where no uops are
being delivered due to a lack of required resources for
accepting new uops in the Backend. Backend is the portion of
the processor core where the out-of-order scheduler
dispatches ready uops into their respective execution units,
and once completed these uops get retired according to
program order. For example, stalls due to data-cache misses
or stalls due to the divider unit being overloaded are both
categorized under Backend Bound. Backend Bound is further
divided into two main categories: Memory Bound and Core
Bound."""
    level = 1
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = 1 -(self.Frontend_Bound.compute(EV) + self.Bad_Speculation.compute(EV) + self.Retiring.compute(EV))
            self.thresh = (self.val > 0.2)
        except ZeroDivisionError:
            print_error("Backend_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Memory_Bound:
    name = "Memory_Bound"
    domain = "Slots"
    area = "BE/Mem"
    desc = """
This metric represents slots fraction the Memory subsystem
within the Backend was a bottleneck.  Memory Bound estimates
slots fraction where pipeline is likely stalled due to
demand load or store instructions. This accounts mainly for
(1) non-completed in-flight memory demand loads which
coincides with execution units starvation, in addition to
(2) cases where stores could impose backpressure on the
pipeline when many of them get buffered at the same time
(less common out of the two)."""
    level = 2
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Memory_Bound_Fraction(self, EV, 2)* self.Backend_Bound.compute(EV )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Memory_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class L1_Bound:
    name = "L1_Bound"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often the CPU was stalled without
loads missing the L1 data cache.  The L1 data cache
typically has the shortest latency.  However, in certain
cases like loads blocked on older stores, a load might
suffer due to high latency even though it is being satisfied
by the L1. Another example is loads who miss in the TLB.
These cases are characterized by execution unit stalls,
while some non-completed demand load lives in the machine
without having that demand load missing the L1 cache."""
    level = 3
    htoff = False
    sample = ['MEM_LOAD_UOPS_RETIRED.L1_HIT:pp', 'MEM_LOAD_UOPS_RETIRED.HIT_LFB:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (STALLS_MEM_ANY(self, EV, 3) - EV("CYCLE_ACTIVITY.STALLS_L1D_PENDING", 3)) / CLKS(self, EV, 3 )
            self.thresh = ((self.val > 0.1) and self.parent.thresh) | self.DTLB_Load.thresh
        except ZeroDivisionError:
            print_error("L1_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class DTLB_Load:
    name = "DTLB_Load"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric represents cycles fraction where the TLB was
missed by load instructions. TLBs (Translation Look-aside
Buffers) are processor caches for recently used entries out
of the Page Tables that are used to map virtual- to
physical-addresses by the operating system. This metric
estimates the performance penalty paid by demand loads when
missing the first-level data TLB (DTLB). This includes
hitting in the second-level TLB (STLB) as well as performing
a hardware page walk on an STLB miss.."""
    level = 4
    htoff = False
    sample = ['MEM_UOPS_RETIRED.STLB_MISS_LOADS:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (Mem_STLB_Hit_Cost * EV("DTLB_LOAD_MISSES.STLB_HIT", 4) + EV("DTLB_LOAD_MISSES.WALK_DURATION", 4)) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1)
        except ZeroDivisionError:
            print_error("DTLB_Load zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Store_Fwd_Blk:
    name = "Store_Fwd_Blk"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric roughly estimates cycles fraction when the
memory subsystem had loads blocked since they could not
forward data from earlier (in program order) overlapping
stores. To streamline memory operations in the pipeline, a
load can avoid waiting for memory if a prior in-flight store
is writing the data that the load wants to read (store
forwarding process). However, in some cases the load may be
blocked for a significant time pending the store forward.
For example, when the prior store is writing a smaller
region than the load is reading."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = 13 * EV("LD_BLOCKS.STORE_FORWARD", 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Store_Fwd_Blk zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Lock_Latency:
    name = "Lock_Latency"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric represents cycles fraction the CPU spent
handling cache misses due to lock operations. Due to the
microarchitecture handling of locks, they are classified as
L1_Bound regardless of what memory source satisfied them."""
    level = 4
    htoff = False
    sample = ['MEM_UOPS_RETIRED.LOCK_LOADS:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Mem_Lock_St_Fraction(self, EV, 4)* ORO_Demand_RFO_C1(self, EV, 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Lock_Latency zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Split_Loads:
    name = "Split_Loads"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction handling memory load
split accesses - load that cross 64-byte cacheline boundary.
. Consider aligning data or hot structure fields. See the
Optimization Guide for more details"""
    level = 4
    htoff = False
    sample = ['MEM_UOPS_RETIRED.SPLIT_LOADS:pp']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = 13 * EV("LD_BLOCKS.NO_SR", 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Split_Loads zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class G4K_Aliasing:
    name = "4K_Aliasing"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often memory load accesses were
aliased by preceding stores (in program order) with a 4K
address offset. False match is possible, which incur a few
cycles load re-issue. However, the short re-issue duration
is often hidden by the out-of-order core and HW
optimizations; hence a user may safely ignore a high value
of this metric unless it manages to propagate up into parent
nodes of the hierarchy (e.g. to L1_Bound).. Consider
reducing independent loads/stores accesses with 4K offsets.
See the Optimization Guide for more details"""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = Mem_4K_Alias_Cost * EV("LD_BLOCKS_PARTIAL.ADDRESS_ALIAS", 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.7) and self.parent.thresh
        except ZeroDivisionError:
            print_error("G4K_Aliasing zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class FB_Full:
    name = "FB_Full"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric does a *rough estimation* of how often L1D Fill
Buffer unavailability limited additional L1D miss memory
access requests to proceed. The higher the metric value, the
deeper the memory hierarchy level the misses are satisfied
from (metric values >1 are valid). Often it hints on
approaching bandwidth limits (to L2 cache, L3 cache or
external memory).. See $issueBW and $issueSL hints. Avoid
adding software prefetches if indeed memory BW limited."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Load_Miss_Real_Latency(self, EV, 4)* EV("L1D_PEND_MISS.FB_FULL:c1", 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.3)
        except ZeroDivisionError:
            print_error("FB_Full zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class L2_Bound:
    name = "L2_Bound"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often the CPU was stalled due to
L2 cache accesses by loads.  Avoiding cache misses (i.e. L1
misses/L2 hits) can improve the latency and increase
performance."""
    level = 3
    htoff = False
    sample = ['MEM_LOAD_UOPS_RETIRED.L2_HIT:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (EV("CYCLE_ACTIVITY.STALLS_L1D_PENDING", 3) - EV("CYCLE_ACTIVITY.STALLS_L2_PENDING", 3)) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("L2_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class L3_Bound:
    name = "L3_Bound"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often the CPU was stalled due to
loads accesses to L3 cache or contended with a sibling Core.
Avoiding cache misses (i.e. L2 misses/L3 hits) can improve
the latency and increase performance."""
    level = 3
    htoff = False
    sample = ['MEM_LOAD_UOPS_RETIRED.LLC_HIT:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Mem_L3_Hit_Fraction(self, EV, 3)* EV("CYCLE_ACTIVITY.STALLS_L2_PENDING", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("L3_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Contested_Accesses:
    name = "Contested_Accesses"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction while the memory
subsystem was handling contested accesses. Contested
accesses occur when data written by one thread are read by
another thread on a different physical core. Examples of
contested accesses include synchronizations such as locks,
true data sharing such as modified locked variables, and
false sharing."""
    level = 4
    htoff = False
    sample = ['MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HIT:pp', 'MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_MISS:pp']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = Mem_XSNP_HitM_Cost *(LOAD_XSNP_HITM(self, EV, 4) + LOAD_XSNP_MISS(self, EV, 4)) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Contested_Accesses zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Data_Sharing:
    name = "Data_Sharing"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction while the memory
subsystem was handling data-sharing accesses. Data shared by
multiple threads (even just read shared) may cause increased
access latency due to cache coherency. Excessive data
sharing can drastically harm multithreaded performance."""
    level = 4
    htoff = False
    sample = ['MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HITM:pp']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = MEM_XSNP_Hit_Cost * LOAD_XSNP_HIT(self, EV, 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Data_Sharing zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class L3_Hit_Latency:
    name = "L3_Hit_Latency"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric represents cycles fraction with demand load
accesses that hit the L3 cache under unloaded scenarios
(possibly L3 latency limited).  Avoiding private cache
misses (i.e. L2 misses/L3 hits) will improve the latency,
reduce contention with sibling physical cores and increase
performance.  Note the value of this node may overlap with
its siblings."""
    level = 4
    htoff = False
    sample = ['MEM_LOAD_UOPS_RETIRED.LLC_HIT:pp']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = MEM_XSNP_None_Cost * LOAD_L3_HIT(self, EV, 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("L3_Hit_Latency zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class SQ_Full:
    name = "SQ_Full"
    domain = "CoreClocks"
    area = "BE/Mem"
    desc = """
This metric measures fraction of cycles where the Super
Queue (SQ) was full taking into account all request-types
and both hardware SMT threads. The Super Queue is used for
requests to access the L2 cache or to go out to the Uncore."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = SQ_Full_Cycles(self, EV, 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.3) and self.parent.thresh
        except ZeroDivisionError:
            print_error("SQ_Full zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class MEM_Bound:
    name = "MEM_Bound"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often the CPU was stalled on
accesses to external memory (DRAM) by loads. Better caching
can improve the latency and increase performance."""
    level = 3
    htoff = False
    sample = ['MEM_LOAD_UOPS_RETIRED.LLC_MISS:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (1 - Mem_L3_Hit_Fraction(self, EV, 3))* EV("CYCLE_ACTIVITY.STALLS_L2_PENDING", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("MEM_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class MEM_Bandwidth:
    name = "MEM_Bandwidth"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction where the core's
performance was likely hurt due to approaching bandwidth
limits of external memory (DRAM).  The underlying heuristic
assumes that a similar off-core traffic is generated by all
IA cores. This metric does not aggregate non-data-read
requests by this thread, requests from other IA
threads/cores/sockets, or other non-IA devices like GPU;
hence the maximum external memory bandwidth limits may or
may not be approached when this metric is flagged (see
Uncore counters for that).. Improve data accesses to reduce
cacheline transfers from/to memory. Examples: 1) Consume all
bytes of a each cacheline before it is evicted (e.g. reorder
structure elements and split non-hot ones), 2) merge
computed-limited with BW-limited loops, 3) NUMA
optimizations in multi-socket system. Note: software
prefetches will not help BW-limited application.."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = ORO_DRD_BW_Cycles(self, EV, 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("MEM_Bandwidth zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class MEM_Latency:
    name = "MEM_Latency"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction where the performance
was likely hurt due to latency from external memory (DRAM).
This metric does not aggregate requests from other
threads/cores/sockets (see Uncore counters for that)..
Improve data accesses or interleave them with compute.
Examples: 1) Data layout re-structuring, 2) Software
Prefetches (also through the compiler).."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = ORO_DRD_Any_Cycles(self, EV, 4) / CLKS(self, EV, 4) - self.MEM_Bandwidth.compute(EV )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("MEM_Latency zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Store_Bound:
    name = "Store_Bound"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates how often CPU was stalled  due to
store memory accesses. Even though store accesses do not
typically stall out-of-order CPUs; there are few cases where
stores can lead to actual stalls. This metric will be
flagged should any of these cases be a bottleneck."""
    level = 3
    htoff = False
    sample = ['MEM_UOPS_RETIRED.ALL_STORES:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("RESOURCE_STALLS.SB", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Store_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Store_Latency:
    name = "Store_Latency"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric estimates cycles fraction the CPU spent handling
L1D store misses. Store accesses usually less impact out-of-
order core performance; however, holding resources for
longer time can lead into undesired implications (e.g.
contention on L1D fill-buffer entries - see FB_Full).
Consider to avoid/reduce unnecessary (or easily load-
able/computable) memory store."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (Store_L2_Hit_Cycles(self, EV, 4) +(1 - Mem_Lock_St_Fraction(self, EV, 4))* ORO_Demand_RFO_C1(self, EV, 4)) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Store_Latency zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class False_Sharing:
    name = "False_Sharing"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric represents how often CPU was stalled due to
False Sharing. False Sharing is a multithreading hiccup,
where multiple threads contend on different data-elements
mapped into the same cache line. . False Sharing can be
easily avoided by padding to make threads access different
lines."""
    level = 4
    htoff = False
    sample = ['MEM_LOAD_UOPS_LLC_HIT_RETIRED.XSNP_HITM:pp', 'OFFCORE_RESPONSE.DEMAND_RFO.LLC_HIT.HITM_OTHER_CORE_0']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = Mem_XSNP_HitM_Cost * EV("OFFCORE_RESPONSE.DEMAND_RFO.LLC_HIT.HITM_OTHER_CORE", 4) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("False_Sharing zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Split_Stores:
    name = "Split_Stores"
    domain = "CoreClocks"
    area = "BE/Mem"
    desc = """
This metric represents rate of split store accesses.
Consider aligning your data to the 64-byte cache line
granularity."""
    level = 4
    htoff = False
    sample = ['MEM_UOPS_RETIRED.SPLIT_STORES:pp']
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = 2 * EV("MEM_UOPS_RETIRED.SPLIT_STORES", 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Split_Stores zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class DTLB_Store:
    name = "DTLB_Store"
    domain = "Clocks"
    area = "BE/Mem"
    desc = """
This metric represents cycles fraction spent handling first-
level data TLB store misses.  As with ordinary data caching,
focus on improving data locality and reducing working-set
size to reduce DTLB overhead.  Additionally, consider using
profile-guided optimization (PGO) to collocate frequently-
used data on the same page.  Try using larger page sizes for
large amounts of frequently-used data."""
    level = 4
    htoff = False
    sample = ['MEM_UOPS_RETIRED.STLB_MISS_STORES:pp']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (Mem_STLB_Hit_Cost * EV("DTLB_STORE_MISSES.STLB_HIT", 4) + EV("DTLB_STORE_MISSES.WALK_DURATION", 4)) / CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.05) and self.parent.thresh
        except ZeroDivisionError:
            print_error("DTLB_Store zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Core_Bound:
    name = "Core_Bound"
    domain = "Slots"
    area = "BE/Core"
    desc = """
This metric represents slots fraction where Core non-memory
issues were of a bottleneck.  Shortage in hardware compute
resources, or dependencies in software's instructions are
both categorized under Core Bound. Hence it may indicate the
machine ran out of an out-of-order resource, certain
execution units are overloaded or dependencies in program's
data- or instruction-flow are limiting the performance (e.g.
FP-chained long-latency arithmetic operations).. Tip:
consider Port Saturation analysis as next step."""
    level = 2
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = self.Backend_Bound.compute(EV) - self.Memory_Bound.compute(EV )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Core_Bound zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Divider:
    name = "Divider"
    domain = "Clocks"
    area = "BE/Core"
    desc = """
This metric represents cycles fraction where the Divider
unit was active. Divide and square root instructions are
performed by the Divider unit and can take considerably
longer latency than integer or Floating Point addition,
subtraction, or multiplication."""
    level = 3
    htoff = False
    sample = ['ARITH.FPU_DIV_ACTIVE']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("ARITH.FPU_DIV_ACTIVE", 3) / CORE_CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Divider zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Ports_Utilization:
    name = "Ports_Utilization"
    domain = "Clocks"
    area = "BE/Core"
    desc = """
This metric estimates cycles fraction the CPU performance
was potentially limited due to Core computation issues (non
divider-related).  Two distinct categories can be attributed
into this metric: (1) heavy data-dependency among contiguous
instructions would manifest in this metric - such cases are
often referred to as low Instruction Level Parallelism
(ILP). (2) Contention on some hardware execution unit other
than Divider. For example, when there are too many multiply
operations.. Loop Vectorization -most compilers feature
auto-Vectorization options today- reduces pressure on the
execution ports as multiple elements are calculated with
same uop."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (Backend_Bound_Cycles(self, EV, 3) - EV("RESOURCE_STALLS.SB", 3) - STALLS_MEM_ANY(self, EV, 3)) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Ports_Utilization zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class G0_Ports_Utilized:
    name = "0_Ports_Utilized"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU executed no
uops on any execution port."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Cycles_0_Ports_Utilized(self, EV, 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("G0_Ports_Utilized zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class G1_Port_Utilized:
    name = "1_Port_Utilized"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction where the CPU
executed total of 1 uop per cycle on all execution ports.
This can be due to heavy data-dependency among software
instructions, or over oversubscribing a particular hardware
resource. In some other cases with high 1_Port_Utilized and
L1_Bound, this metric can point to L1 data-cache latency
bottleneck that may not necessarily manifest with complete
execution starvation (due to the short L1 latency e.g.
walking a linked list) - looking at the assembly can be
helpful. Tip: consider 'Core Ports Saturation' analysis-type
as next step."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Cycles_1_Port_Utilized(self, EV, 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("G1_Port_Utilized zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class G2_Ports_Utilized:
    name = "2_Ports_Utilized"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU executed
total of 2 uops per cycle on all execution ports. Tip:
consider 'Core Port Saturation' analysis-type as next step.
Loop Vectorization -most compilers feature auto-
Vectorization options today- reduces pressure on the
execution ports as multiple elements are calculated with
same uop."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Cycles_2_Ports_Utilized(self, EV, 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("G2_Ports_Utilized zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class G3m_Ports_Utilized:
    name = "3m_Ports_Utilized"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU executed
total of 3 or more uops per cycle on all execution ports.
Tip: consider 'Core Port Saturation' analysis-type as next
step"""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Cycles_3m_Ports_Utilized(self, EV, 4) / CORE_CLKS(self, EV, 4 )
            self.thresh = (self.val > 0.4) and self.parent.thresh
        except ZeroDivisionError:
            print_error("G3m_Ports_Utilized zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_0:
    name = "Port_0"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 0 (SNB+: ALU; HSW+:ALU and 2nd
branch)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_0", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_0 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_1:
    name = "Port_1"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 1 (ALU)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_1", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_1 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_2:
    name = "Port_2"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 2 (Loads and Store-address)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_2", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_2 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_3:
    name = "Port_3"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 3 (Loads and Store-address)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_3", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_3 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_4:
    name = "Port_4"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 4 (Store-data)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_4", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_4 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Port_5:
    name = "Port_5"
    domain = "CoreClocks"
    area = "BE/Core"
    desc = """
This metric represents Core cycles fraction CPU dispatched
uops on execution port 5 (SNB+: Branches and ALU; HSW+: ALU)"""
    level = 5
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = EV("UOPS_DISPATCHED_PORT.PORT_5", 5) / CORE_CLKS(self, EV, 5 )
            self.thresh = (self.val > 0.6)
        except ZeroDivisionError:
            print_error("Port_5 zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Retiring:
    name = "Retiring"
    domain = "Slots"
    area = "RET"
    desc = """
This category represents slots fraction utilized by useful
work i.e. issued uops that eventually get retired. Ideally,
all pipeline slots would be attributed to the Retiring
category.  Retiring of 100% would indicate the maximum 4
uops retired per cycle has been achieved.  Maximizing
Retiring typically increases the Instruction-Per-Cycle
metric. Note that a high Retiring value does not necessary
mean there is no room for more performance.  For example,
Microcode assists are categorized under Retiring. They hurt
performance and can often be avoided. . A high Retiring
value for non-vectorized code may be a good hint for
programmer to consider vectorizing his code.  Doing so
essentially lets more computations be done without
significantly increasing number of instructions thus
improving the performance."""
    level = 1
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("UOPS_RETIRED.RETIRE_SLOTS", 1) / SLOTS(self, EV, 1 )
            self.thresh = (self.val > 0.7) | self.Microcode_Sequencer.thresh
        except ZeroDivisionError:
            print_error("Retiring zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Base:
    name = "Base"
    domain = "Slots"
    area = "RET"
    desc = """
This metric represents slots fraction where the CPU was
retiring regular uops (ones not originated from the
microcode-sequencer). This correlates with total number of
instructions used by the program. A uops-per-instruction
ratio of 1 should be expected. While this is the most
desirable of the top 4 categories, high values does not
necessarily mean there no room for performance
optimizations.. Focus on techniques that reduce instruction
count or result in more efficient instructions generation
such as vectorization."""
    level = 2
    htoff = False
    sample = ['INST_RETIRED.PREC_DIST']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = self.Retiring.compute(EV) - self.Microcode_Sequencer.compute(EV )
            self.thresh = (self.val > 0.6) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Base zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class FP_Arith:
    name = "FP_Arith"
    domain = "Uops"
    area = "RET"
    desc = """
This metric represents overall arithmetic floating-point
(FP) uops fraction the CPU has executed (retired)"""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = self.X87_Use.compute(EV) + self.FP_Scalar.compute(EV) + self.FP_Vector.compute(EV )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("FP_Arith zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class X87_Use:
    name = "X87_Use"
    domain = "Uops"
    area = "RET"
    desc = """
This metric serves as an approximation of legacy x87 usage.
It accounts for instructions beyond X87 FP arithmetic
operations; hence may be used as a thermometer to avoid X87
high usage and preferably upgrade to modern ISA. Tip:
consider compiler flags to generate newer AVX (or SSE)
instruction sets, which typically perform better and feature
vectors."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = EV("FP_COMP_OPS_EXE.X87", 4) / EV("UOPS_EXECUTED.THREAD", 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("X87_Use zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class FP_Scalar:
    name = "FP_Scalar"
    domain = "Uops"
    area = "RET"
    desc = """
This metric represents arithmetic floating-point (FP) scalar
uops fraction the CPU has executed (retired).. Investigate
what limits (compiler) generation of vector code."""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (EV("FP_COMP_OPS_EXE.SSE_SCALAR_SINGLE", 4) + EV("FP_COMP_OPS_EXE.SSE_SCALAR_DOUBLE", 4)) / EV("UOPS_EXECUTED.THREAD", 4 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("FP_Scalar zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class FP_Vector:
    name = "FP_Vector"
    domain = "Uops"
    area = "RET"
    desc = """
This metric represents arithmetic floating-point (FP) vector
uops fraction the CPU has executed (retired) aggregated
across all vector widths.. Check if vector width is expected"""
    level = 4
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = (EV("FP_COMP_OPS_EXE.SSE_PACKED_DOUBLE", 4) + EV("FP_COMP_OPS_EXE.SSE_PACKED_SINGLE", 4) + EV("SIMD_FP_256.PACKED_SINGLE", 4) + EV("SIMD_FP_256.PACKED_DOUBLE", 4)) / EV("UOPS_EXECUTED.THREAD", 4 )
            self.thresh = (self.val > 0.2) and self.parent.thresh
        except ZeroDivisionError:
            print_error("FP_Vector zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Other:
    name = "Other"
    domain = "Uops"
    area = "RET"
    desc = """
This metric represents non-floating-point (FP) uop fraction
the CPU has executed. If you application has no FP
operations and performs with decent IPC (Instructions Per
Cycle), this node will likely be biggest fraction."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = 1 - self.FP_Arith.compute(EV )
            self.thresh = (self.val > 0.3) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Other zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Microcode_Sequencer:
    name = "Microcode_Sequencer"
    domain = "Slots"
    area = "RET"
    desc = """
This metric represents slots fraction the CPU was retiring
uops fetched by the Microcode Sequencer (MS) unit.  The MS
is used for CISC instructions not supported by the default
decoders (like repeat move strings, or CPUID), or by
microcode assists used to address some operation modes (like
in Floating Point assists). These cases can often be
avoided.."""
    level = 2
    htoff = False
    sample = ['IDQ.MS_UOPS']
    errcount = 0
    sibling = None
    server = True
    def compute(self, EV):
        try:
            self.val = Retire_Uop_Fraction(self, EV, 2)* EV("IDQ.MS_UOPS", 2) / SLOTS(self, EV, 2 )
            self.thresh = (self.val > 0.05)
        except ZeroDivisionError:
            print_error("Microcode_Sequencer zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Assists:
    name = "Assists"
    domain = "Clocks"
    area = "RET"
    desc = """
This metric estimates cycles fraction the CPU retired uops
delivered by the Microcode_Sequencer as a result of Assists.
Assists are long sequences of uops that are required in
certain corner-cases for operations that cannot be handled
natively by the execution pipeline. For example, when
working with very small floating point values (so-called
Denormals), the FP units are not set up to perform these
operations natively. Instead, a sequence of instructions to
perform the computation on the Denormals is injected into
the pipeline. Since these microcode sequences might be
hundreds of uops long, Assists can be extremely deleterious
to performance and they can be avoided in many cases."""
    level = 3
    htoff = False
    sample = []
    errcount = 0
    sibling = None
    server = False
    def compute(self, EV):
        try:
            self.val = 300 * EV("OTHER_ASSISTS.ANY_WB_ASSIST", 3) / CLKS(self, EV, 3 )
            self.thresh = (self.val > 0.1) and self.parent.thresh
        except ZeroDivisionError:
            print_error("Assists zero division")
            self.errcount += 1
            self.val = 0
            self.thresh = False
        return self.val

class Metric_IPC:
    name = "IPC"
    desc = """
Instructions Per Cycle (per logical thread)"""
    domain = "Metric"
    maxval = 5
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = IPC(self, EV, 0)
        except ZeroDivisionError:
            print_error("IPC zero division")
            self.errcount += 1
	    self.val = 0

class Metric_UPI:
    name = "UPI"
    desc = """
Uops Per Instruction"""
    domain = "Metric"
    maxval = 2
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = UPI(self, EV, 0)
        except ZeroDivisionError:
            print_error("UPI zero division")
            self.errcount += 1
	    self.val = 0

class Metric_IPTB:
    name = "IPTB"
    desc = """
Instruction per taken branch"""
    domain = "Metric"
    maxval = 0
    server = False
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = IPTB(self, EV, 0)
        except ZeroDivisionError:
            print_error("IPTB zero division")
            self.errcount += 1
	    self.val = 0

class Metric_BPTB:
    name = "BPTB"
    desc = """
Branch instructions per taken branch. Can be used to
approximate PGO-likelihood for non-loopy codes."""
    domain = "Metric"
    maxval = 0
    server = False
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = BPTB(self, EV, 0)
        except ZeroDivisionError:
            print_error("BPTB zero division")
            self.errcount += 1
	    self.val = 0

class Metric_IFetch_Line_Utilization:
    name = "IFetch_Line_Utilization"
    desc = """
Rough Estimation of fraction of fetched lines bytes that
were likely consumed by program instructions"""
    domain = "Metric"
    maxval = 1
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = IFetch_Line_Utilization(self, EV, 0)
        except ZeroDivisionError:
            print_error("IFetch_Line_Utilization zero division")
            self.errcount += 1
	    self.val = 0

class Metric_DSB_Coverage:
    name = "DSB_Coverage"
    desc = """
Fraction of Uops delivered by the DSB (decoded instructions
cache)"""
    domain = "Metric"
    maxval = 1
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = DSB_Coverage(self, EV, 0)
        except ZeroDivisionError:
            print_error("DSB_Coverage zero division")
            self.errcount += 1
	    self.val = 0

class Metric_CPI:
    name = "CPI"
    desc = """
Cycles Per Instruction (threaded)"""
    domain = "Metric"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = CPI(self, EV, 0)
        except ZeroDivisionError:
            print_error("CPI zero division")
            self.errcount += 1
	    self.val = 0

class Metric_CLKS:
    name = "CLKS"
    desc = """
Per-thread actual clocks when the thread is active"""
    domain = "Count"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = CLKS(self, EV, 0)
        except ZeroDivisionError:
            print_error("CLKS zero division")
            self.errcount += 1
	    self.val = 0

class Metric_SLOTS:
    name = "SLOTS"
    desc = """
Total issue-pipeline slots"""
    domain = "Count"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = SLOTS(self, EV, 0)
        except ZeroDivisionError:
            print_error("SLOTS zero division")
            self.errcount += 1
	    self.val = 0

class Metric_CoreIPC:
    name = "CoreIPC"
    desc = """
Instructions Per Cycle (per physical core)"""
    domain = "CoreMetric"
    maxval = 5
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = CoreIPC(self, EV, 0)
        except ZeroDivisionError:
            print_error("CoreIPC zero division")
            self.errcount += 1
	    self.val = 0

class Metric_FLOPc:
    name = "FLOPc"
    desc = """
Floating Point Operations Per Cycle"""
    domain = "CoreMetric"
    maxval = 10
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = FLOPc(self, EV, 0)
        except ZeroDivisionError:
            print_error("FLOPc zero division")
            self.errcount += 1
	    self.val = 0

class Metric_ILP:
    name = "ILP"
    desc = """
Instruction-Level-Parallelism (average number of uops
executed when there is at least 1 uop executed)"""
    domain = "CoreMetric"
    maxval = 10
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = ILP(self, EV, 0)
        except ZeroDivisionError:
            print_error("ILP zero division")
            self.errcount += 1
	    self.val = 0

class Metric_MLP:
    name = "MLP"
    desc = """
Memory-Level-Parallelism (average number of L1 miss demand
load when there is at least 1 such miss)"""
    domain = "CoreMetric"
    maxval = 10
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = MLP(self, EV, 0)
        except ZeroDivisionError:
            print_error("MLP zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Page_Walks_Use:
    name = "Page_Walks_Use"
    desc = """
Utilization of the core's Page Walker(s) serving STLB misses
triggered by instruction/Load/Store accesses"""
    domain = "CoreMetric"
    maxval = 1
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Page_Walks_Use(self, EV, 0)
        except ZeroDivisionError:
            print_error("Page_Walks_Use zero division")
            self.errcount += 1
	    self.val = 0

class Metric_CORE_CLKS:
    name = "CORE_CLKS"
    desc = """
Core actual clocks when any thread is active on the physical
core"""
    domain = "Count"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = CORE_CLKS(self, EV, 0)
        except ZeroDivisionError:
            print_error("CORE_CLKS zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Load_Miss_Real_Latency:
    name = "Load_Miss_Real_Latency"
    desc = """
Actual Average Latency for L1 data-cache miss demand loads"""
    domain = "Metric"
    maxval = 1000
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Load_Miss_Real_Latency(self, EV, 0)
        except ZeroDivisionError:
            print_error("Load_Miss_Real_Latency zero division")
            self.errcount += 1
	    self.val = 0

class Metric_CPU_Utilization:
    name = "CPU_Utilization"
    desc = """
Average CPU Utilization"""
    domain = "Metric"
    maxval = 100
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = CPU_Utilization(self, EV, 0)
        except ZeroDivisionError:
            print_error("CPU_Utilization zero division")
            self.errcount += 1
	    self.val = 0

class Metric_GFLOPs:
    name = "GFLOPs"
    desc = """
Giga Floating Point Operations Per Second"""
    domain = "Metric"
    maxval = 100
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = GFLOPs(self, EV, 0)
        except ZeroDivisionError:
            print_error("GFLOPs zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Turbo_Utilization:
    name = "Turbo_Utilization"
    desc = """
Average Frequency Utilization relative nominal frequency"""
    domain = "CoreMetric"
    maxval = 10
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Turbo_Utilization(self, EV, 0)
        except ZeroDivisionError:
            print_error("Turbo_Utilization zero division")
            self.errcount += 1
	    self.val = 0

class Metric_SMT_2T_Utilization:
    name = "SMT_2T_Utilization"
    desc = """
Fraction of cycles where both hardware threads were active"""
    domain = "CoreMetric"
    maxval = 1
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = SMT_2T_Utilization(self, EV, 0)
        except ZeroDivisionError:
            print_error("SMT_2T_Utilization zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Kernel_Utilization:
    name = "Kernel_Utilization"
    desc = """
Fraction of cycles spent in Kernel mode"""
    domain = "Metric"
    maxval = 1
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Kernel_Utilization(self, EV, 0)
        except ZeroDivisionError:
            print_error("Kernel_Utilization zero division")
            self.errcount += 1
	    self.val = 0

class Metric_MEM_BW_GBs:
    name = "MEM_BW_GBs"
    desc = """
Average external Memory Bandwidth Use for reads and writes
[GB / sec]"""
    domain = "Metric"
    maxval = 100
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = MEM_BW_GBs(self, EV, 0)
        except ZeroDivisionError:
            print_error("MEM_BW_GBs zero division")
            self.errcount += 1
	    self.val = 0

class Metric_MEM_Request_Latency:
    name = "MEM_Request_Latency"
    desc = """
Average latency of all requests to external memory (in
Uncore cycles)"""
    domain = "Metric"
    maxval = 1000
    server = False
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = MEM_Request_Latency(self, EV, 0)
        except ZeroDivisionError:
            print_error("MEM_Request_Latency zero division")
            self.errcount += 1
	    self.val = 0

class Metric_MEM_Parallel_Requests:
    name = "MEM_Parallel_Requests"
    desc = """
Average number of parallel requests to external memory (in
Uncore cycles). Accounts for all requests"""
    domain = "Metric"
    maxval = 100
    server = False
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = MEM_Parallel_Requests(self, EV, 0)
        except ZeroDivisionError:
            print_error("MEM_Parallel_Requests zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Time:
    name = "Time"
    desc = """
Run duration time in seconds"""
    domain = "Count"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Time(self, EV, 0)
        except ZeroDivisionError:
            print_error("Time zero division")
            self.errcount += 1
	    self.val = 0

class Metric_Socket_CLKS:
    name = "Socket_CLKS"
    desc = """
"""
    domain = "Count"
    maxval = 0
    server = True
    errcount = 0

    def compute(self, EV):
        try:
	    self.val = Socket_CLKS(self, EV, 0)
        except ZeroDivisionError:
            print_error("Socket_CLKS zero division")
            self.errcount += 1
	    self.val = 0

# Schedule



class Setup:
    def __init__(self, r):
	o = dict()
        n = Frontend_Bound() ; r.run(n) ; o["Frontend_Bound"] = n
        n = Frontend_Latency() ; r.run(n) ; o["Frontend_Latency"] = n
        n = ICache_Misses() ; r.run(n) ; o["ICache_Misses"] = n
        n = ITLB_Misses() ; r.run(n) ; o["ITLB_Misses"] = n
        n = Branch_Resteers() ; r.run(n) ; o["Branch_Resteers"] = n
        n = DSB_Switches() ; r.run(n) ; o["DSB_Switches"] = n
        n = LCP() ; r.run(n) ; o["LCP"] = n
        n = MS_Switches() ; r.run(n) ; o["MS_Switches"] = n
        n = Frontend_Bandwidth() ; r.run(n) ; o["Frontend_Bandwidth"] = n
        n = MITE() ; r.run(n) ; o["MITE"] = n
        n = DSB() ; r.run(n) ; o["DSB"] = n
        n = LSD() ; r.run(n) ; o["LSD"] = n
        n = Bad_Speculation() ; r.run(n) ; o["Bad_Speculation"] = n
        n = Branch_Mispredicts() ; r.run(n) ; o["Branch_Mispredicts"] = n
        n = Machine_Clears() ; r.run(n) ; o["Machine_Clears"] = n
        n = Backend_Bound() ; r.run(n) ; o["Backend_Bound"] = n
        n = Memory_Bound() ; r.run(n) ; o["Memory_Bound"] = n
        n = L1_Bound() ; r.run(n) ; o["L1_Bound"] = n
        n = DTLB_Load() ; r.run(n) ; o["DTLB_Load"] = n
        n = Store_Fwd_Blk() ; r.run(n) ; o["Store_Fwd_Blk"] = n
        n = Lock_Latency() ; r.run(n) ; o["Lock_Latency"] = n
        n = Split_Loads() ; r.run(n) ; o["Split_Loads"] = n
        n = G4K_Aliasing() ; r.run(n) ; o["G4K_Aliasing"] = n
        n = FB_Full() ; r.run(n) ; o["FB_Full"] = n
        n = L2_Bound() ; r.run(n) ; o["L2_Bound"] = n
        n = L3_Bound() ; r.run(n) ; o["L3_Bound"] = n
        n = Contested_Accesses() ; r.run(n) ; o["Contested_Accesses"] = n
        n = Data_Sharing() ; r.run(n) ; o["Data_Sharing"] = n
        n = L3_Hit_Latency() ; r.run(n) ; o["L3_Hit_Latency"] = n
        n = SQ_Full() ; r.run(n) ; o["SQ_Full"] = n
        n = MEM_Bound() ; r.run(n) ; o["MEM_Bound"] = n
        n = MEM_Bandwidth() ; r.run(n) ; o["MEM_Bandwidth"] = n
        n = MEM_Latency() ; r.run(n) ; o["MEM_Latency"] = n
        n = Store_Bound() ; r.run(n) ; o["Store_Bound"] = n
        n = Store_Latency() ; r.run(n) ; o["Store_Latency"] = n
        n = False_Sharing() ; r.run(n) ; o["False_Sharing"] = n
        n = Split_Stores() ; r.run(n) ; o["Split_Stores"] = n
        n = DTLB_Store() ; r.run(n) ; o["DTLB_Store"] = n
        n = Core_Bound() ; r.run(n) ; o["Core_Bound"] = n
        n = Divider() ; r.run(n) ; o["Divider"] = n
        n = Ports_Utilization() ; r.run(n) ; o["Ports_Utilization"] = n
        n = G0_Ports_Utilized() ; r.run(n) ; o["G0_Ports_Utilized"] = n
        n = G1_Port_Utilized() ; r.run(n) ; o["G1_Port_Utilized"] = n
        n = G2_Ports_Utilized() ; r.run(n) ; o["G2_Ports_Utilized"] = n
        n = G3m_Ports_Utilized() ; r.run(n) ; o["G3m_Ports_Utilized"] = n
        n = Port_0() ; r.run(n) ; o["Port_0"] = n
        n = Port_1() ; r.run(n) ; o["Port_1"] = n
        n = Port_2() ; r.run(n) ; o["Port_2"] = n
        n = Port_3() ; r.run(n) ; o["Port_3"] = n
        n = Port_4() ; r.run(n) ; o["Port_4"] = n
        n = Port_5() ; r.run(n) ; o["Port_5"] = n
        n = Retiring() ; r.run(n) ; o["Retiring"] = n
        n = Base() ; r.run(n) ; o["Base"] = n
        n = FP_Arith() ; r.run(n) ; o["FP_Arith"] = n
        n = X87_Use() ; r.run(n) ; o["X87_Use"] = n
        n = FP_Scalar() ; r.run(n) ; o["FP_Scalar"] = n
        n = FP_Vector() ; r.run(n) ; o["FP_Vector"] = n
        n = Other() ; r.run(n) ; o["Other"] = n
        n = Microcode_Sequencer() ; r.run(n) ; o["Microcode_Sequencer"] = n
        n = Assists() ; r.run(n) ; o["Assists"] = n

        # parents

        o["Frontend_Latency"].parent = o["Frontend_Bound"]
        o["ICache_Misses"].parent = o["Frontend_Latency"]
        o["ITLB_Misses"].parent = o["Frontend_Latency"]
        o["Branch_Resteers"].parent = o["Frontend_Latency"]
        o["DSB_Switches"].parent = o["Frontend_Latency"]
        o["LCP"].parent = o["Frontend_Latency"]
        o["MS_Switches"].parent = o["Frontend_Latency"]
        o["Frontend_Bandwidth"].parent = o["Frontend_Bound"]
        o["MITE"].parent = o["Frontend_Bandwidth"]
        o["DSB"].parent = o["Frontend_Bandwidth"]
        o["LSD"].parent = o["Frontend_Bandwidth"]
        o["Branch_Mispredicts"].parent = o["Bad_Speculation"]
        o["Machine_Clears"].parent = o["Bad_Speculation"]
        o["Memory_Bound"].parent = o["Backend_Bound"]
        o["L1_Bound"].parent = o["Memory_Bound"]
        o["DTLB_Load"].parent = o["L1_Bound"]
        o["Store_Fwd_Blk"].parent = o["L1_Bound"]
        o["Lock_Latency"].parent = o["L1_Bound"]
        o["Split_Loads"].parent = o["L1_Bound"]
        o["G4K_Aliasing"].parent = o["L1_Bound"]
        o["FB_Full"].parent = o["L1_Bound"]
        o["L2_Bound"].parent = o["Memory_Bound"]
        o["L3_Bound"].parent = o["Memory_Bound"]
        o["Contested_Accesses"].parent = o["L3_Bound"]
        o["Data_Sharing"].parent = o["L3_Bound"]
        o["L3_Hit_Latency"].parent = o["L3_Bound"]
        o["SQ_Full"].parent = o["L3_Bound"]
        o["MEM_Bound"].parent = o["Memory_Bound"]
        o["MEM_Bandwidth"].parent = o["MEM_Bound"]
        o["MEM_Latency"].parent = o["MEM_Bound"]
        o["Store_Bound"].parent = o["Memory_Bound"]
        o["Store_Latency"].parent = o["Store_Bound"]
        o["False_Sharing"].parent = o["Store_Bound"]
        o["Split_Stores"].parent = o["Store_Bound"]
        o["DTLB_Store"].parent = o["Store_Bound"]
        o["Core_Bound"].parent = o["Backend_Bound"]
        o["Divider"].parent = o["Core_Bound"]
        o["Ports_Utilization"].parent = o["Core_Bound"]
        o["G0_Ports_Utilized"].parent = o["Ports_Utilization"]
        o["G1_Port_Utilized"].parent = o["Ports_Utilization"]
        o["G2_Ports_Utilized"].parent = o["Ports_Utilization"]
        o["G3m_Ports_Utilized"].parent = o["Ports_Utilization"]
        o["Port_0"].parent = o["G3m_Ports_Utilized"]
        o["Port_1"].parent = o["G3m_Ports_Utilized"]
        o["Port_2"].parent = o["G3m_Ports_Utilized"]
        o["Port_3"].parent = o["G3m_Ports_Utilized"]
        o["Port_4"].parent = o["G3m_Ports_Utilized"]
        o["Port_5"].parent = o["G3m_Ports_Utilized"]
        o["Base"].parent = o["Retiring"]
        o["FP_Arith"].parent = o["Base"]
        o["X87_Use"].parent = o["FP_Arith"]
        o["FP_Scalar"].parent = o["FP_Arith"]
        o["FP_Vector"].parent = o["FP_Arith"]
        o["Other"].parent = o["Base"]
        o["Microcode_Sequencer"].parent = o["Retiring"]
        o["Assists"].parent = o["Microcode_Sequencer"]

        # references between groups

        o["ICache_Misses"].ITLB_Misses = o["ITLB_Misses"]
        o["Frontend_Bandwidth"].Frontend_Bound = o["Frontend_Bound"]
        o["Frontend_Bandwidth"].Frontend_Latency = o["Frontend_Latency"]
        o["Branch_Mispredicts"].Bad_Speculation = o["Bad_Speculation"]
        o["Machine_Clears"].Bad_Speculation = o["Bad_Speculation"]
        o["Machine_Clears"].Branch_Mispredicts = o["Branch_Mispredicts"]
        o["Backend_Bound"].Retiring = o["Retiring"]
        o["Backend_Bound"].Bad_Speculation = o["Bad_Speculation"]
        o["Backend_Bound"].Frontend_Bound = o["Frontend_Bound"]
        o["Memory_Bound"].Backend_Bound = o["Backend_Bound"]
        o["Memory_Bound"].Frontend_Latency = o["Frontend_Latency"]
        o["L1_Bound"].DTLB_Load = o["DTLB_Load"]
        o["MEM_Latency"].MEM_Bandwidth = o["MEM_Bandwidth"]
        o["Core_Bound"].Memory_Bound = o["Memory_Bound"]
        o["Core_Bound"].Backend_Bound = o["Backend_Bound"]
        o["Ports_Utilization"].Frontend_Latency = o["Frontend_Latency"]
        o["G0_Ports_Utilized"].Frontend_Latency = o["Frontend_Latency"]
        o["Retiring"].Microcode_Sequencer = o["Microcode_Sequencer"]
        o["Base"].Retiring = o["Retiring"]
        o["Base"].Microcode_Sequencer = o["Microcode_Sequencer"]
        o["FP_Arith"].FP_Scalar = o["FP_Scalar"]
        o["FP_Arith"].X87_Use = o["X87_Use"]
        o["FP_Arith"].FP_Vector = o["FP_Vector"]
        o["Other"].FP_Arith = o["FP_Arith"]

        # siblings cross-tree

	o["Branch_Resteers"].sibling = o["Bad_Speculation"]
	o["MS_Switches"].sibling = o["Microcode_Sequencer"]
	o["Bad_Speculation"].sibling = o["Branch_Resteers"]
	o["L1_Bound"].sibling = o["G1_Port_Utilized"]
	o["Lock_Latency"].sibling = o["Store_Latency"]
	o["FB_Full"].sibling = o["SQ_Full"]
	o["Contested_Accesses"].sibling = o["False_Sharing"]
	o["SQ_Full"].sibling = o["FB_Full"]
	o["MEM_Bandwidth"].sibling = o["FB_Full"]
	o["Store_Latency"].sibling = o["Lock_Latency"]
	o["False_Sharing"].sibling = o["Contested_Accesses"]
	o["Split_Stores"].sibling = o["Port_4"]
	o["G1_Port_Utilized"].sibling = o["L1_Bound"]
	o["Port_4"].sibling = o["Split_Stores"]
	o["Microcode_Sequencer"].sibling = o["MS_Switches"]

        # user visible metrics

        n = Metric_IPC() ; r.metric(n)
        n = Metric_UPI() ; r.metric(n)
        n = Metric_IPTB() ; r.metric(n)
        n = Metric_BPTB() ; r.metric(n)
        n = Metric_IFetch_Line_Utilization() ; r.metric(n)
        n = Metric_DSB_Coverage() ; r.metric(n)
        n = Metric_CPI() ; r.metric(n)
        n = Metric_CLKS() ; r.metric(n)
        n = Metric_SLOTS() ; r.metric(n)
        n = Metric_CoreIPC() ; r.metric(n)
        n = Metric_FLOPc() ; r.metric(n)
        n = Metric_ILP() ; r.metric(n)
        n = Metric_MLP() ; r.metric(n)
        n = Metric_Page_Walks_Use() ; r.metric(n)
        n = Metric_CORE_CLKS() ; r.metric(n)
        n = Metric_Load_Miss_Real_Latency() ; r.metric(n)
        n = Metric_CPU_Utilization() ; r.metric(n)
        n = Metric_GFLOPs() ; r.metric(n)
        n = Metric_Turbo_Utilization() ; r.metric(n)
        n = Metric_SMT_2T_Utilization() ; r.metric(n)
        n = Metric_Kernel_Utilization() ; r.metric(n)
        n = Metric_MEM_BW_GBs() ; r.metric(n)
        n = Metric_MEM_Request_Latency() ; r.metric(n)
        n = Metric_MEM_Parallel_Requests() ; r.metric(n)
        n = Metric_Time() ; r.metric(n)
        n = Metric_Socket_CLKS() ; r.metric(n)
