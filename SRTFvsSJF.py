#Pre-Emptive SJF
pros = [
    ["P1", 0, 16],
    ["P2", 1, 5],
    ["P3", 2, 6],
    ["P4", 3, 1],
    ["P5", 4, 2]
]

n = len(pros)
interval = 4

remaining = [p[2] for p in pros]
ct = [0] * n
tat = [0] * n
wt = [0] * n
time = 0
completed = 0
serial = []

while completed < n:

    shortest = -1
    min_remaining = float('inf')

    for i in range(n):
        pid, at, bt = pros[i]
        if at <= time and remaining[i] > 0:

            if remaining[i] < min_remaining:
                min_remaining = remaining[i]
                shortest = i

    if shortest == -1:
        time += 1
        continue

    serial.append(pros[shortest][0])
    run_time = min(interval, remaining[shortest])
    remaining[shortest] -= run_time
    time += run_time

    if remaining[shortest] == 0:
        completed += 1
        ct[shortest] = time

        at = pros[shortest][1]
        bt = pros[shortest][2]

        tat[shortest] = ct[shortest] - at
        wt[shortest] = tat[shortest] - bt

results = []

for i in range(n):
    results.append([
        pros[i][0], pros[i][1],pros[i][2], ct[i], tat[i], wt[i]
    ])
results.sort(key=lambda x: int(x[0][1:]))
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
total_tat = 0
total_wt = 0

for process in results:
    pid, at, bt, ct_value, tat_value, wt_value = process

    print(
        pid, "\t", at, "\t",bt, "\t",ct_value, "\t", tat_value, "\t", wt_value
    )

    total_tat += tat_value
    total_wt += wt_value

preemptive_avg_tat = total_tat / n
preemptive_avg_wt = total_wt / n

print("\nAverage TAT =", preemptive_avg_tat)
print("Average WT =", preemptive_avg_wt)
print("The Pre-emptive SJF Serial:")
print(" -> ".join(serial), "-> Done")

#Non Pre-Emptive SJF
pros = [
    ["P1", 0, 16],
    ["P2", 1, 5],
    ["P3", 2, 6],
    ["P4", 3, 1],
    ["P5", 4, 2]
]

n = len(pros)
time = 0
completed = []
total_tat = 0
total_wt = 0
results = []

while len(completed) < n:
    available = []

    for process in pros:
        pid, at, bt = process
        if pid not in completed and at <= time:
            available.append(process)

    if len(available) == 0:
        time = min(
            p[1]
            for p in pros
            if p[0] not in completed
        )
        continue
        
    available.sort(key=lambda x: (x[2], x[1]))
    pid, at, bt = available[0]
    ct = time + bt
    tat = ct - at
    wt = tat - bt
    results.append([
        pid,at,bt,ct, tat, wt
    ])

    total_tat += tat
    total_wt += wt
    time = ct
    completed.append(pid)

execution_order = sorted(results, key=lambda x: x[3])

results.sort(key=lambda x: int(x[0][1:]))
print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for process in results:
    pid, at, bt, ct, tat, wt = process

    print(
        pid, "\t",  at, "\t",   bt, "\t",  ct, "\t",  tat, "\t",wt
    )

non_preemptive_avg_tat = total_tat / n
non_preemptive_avg_wt = total_wt / n

print("\nAverage TAT =", non_preemptive_avg_tat)
print("Average WT =", non_preemptive_avg_wt)
print("The Non-Pre-emptive SJF Serial:")

for process in execution_order:
    print(process[0], end=" -> ")

print("Done")
print("Pre-emptive SJF VS Non-Pre-emptive SJF:")
print("Operation\t\tAverage TAT\tAverage WT")

print(
    f"Pre-emptive SJF\t\t"
    f"{preemptive_avg_tat:.1f}\t\t"
    f"{preemptive_avg_wt:.1f}"
)

print(
    f"Non-Pre-emptive SJF\t"
    f"{non_preemptive_avg_tat:.1f}\t\t"
    f"{non_preemptive_avg_wt:.1f}"
)
print("\nBest Algorithm:")

if preemptive_avg_tat < non_preemptive_avg_tat and preemptive_avg_wt < non_preemptive_avg_wt:
    print("Pre-emptive SJF is better.")
    print("Reason: It has lower Average TAT and Average WT.")

elif non_preemptive_avg_tat < preemptive_avg_tat and non_preemptive_avg_wt < preemptive_avg_wt:
    print("Non-Pre-emptive SJF is better.")
    print("Reason: It has lower Average TAT and Average WT.")

else:
    print("Both algorithms have similar performance.")
    print("The better algorithm depends on the Average TAT and Average WT.")
