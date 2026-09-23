# Non-Preemptive Priority Scheduling
pros = [
    ["P1", 3, 4, 2],
    ["P2", 1, 2, 1],
    ["P3", 0, 3, 3],
    ["P4", 4, 2, 1],
    ["P5", 6, 4, 3],
    ["P6", 9, 6, 0]
]

n = len(pros)

completed = []
c_time = 0
results = []

while len(completed) < n:

    available = [
        p for p in pros
        if p[0] not in completed and p[1] <= c_time
    ]

    if not available:
        c_time += 1
        continue

    selected = min(available, key=lambda x: x[3])

    pid, at, bt, priority = selected

    c_time += bt
    ct = c_time

    tat = ct - at
    wt = tat - bt

    results.append([pid, at, bt, priority, ct, tat, wt])
    completed.append(pid)


print("\nPriority Scheduling : Non-Preemptive\n")

print(
    f"{'PID':<8}"
    f"{'AT':<8}"
    f"{'BT':<8}"
    f"{'Priority':<10}"
    f"{'CT':<8}"
    f"{'TAT':<8}"
    f"{'WT':<8}"
)

table_results = sorted(results, key=lambda x: x[0])

for r in table_results:
    print(
        f"{r[0]:<8}"
        f"{r[1]:<8}"
        f"{r[2]:<8}"
        f"{r[3]:<10}"
        f"{r[4]:<8}"
        f"{r[5]:<8}"
        f"{r[6]:<8}"
    )


avg_tat = sum(r[5] for r in results) / n
avg_wt = sum(r[6] for r in results) / n

print(f"\nAverage TAT = {avg_tat:.2f}")
print(f"Average WT  = {avg_wt:.2f}")


print("\nNon Preemptive Priority Scheduling Execution Order:")
print(" -> ".join(r[0] for r in results), "-> Done")

#Preemptive Priority Scheduling
pros = [
    ["P1", 3, 4, 2],
    ["P2", 1, 2, 1],
    ["P3", 0, 3, 3],
    ["P4", 4, 2, 1],
    ["P5", 6, 4, 3],
    ["P6", 9, 6, 0]
]

n = len(pros)

remain = {p[0]: p[2] for p in pros}

completion = {}
c_time = 0
execution_order = []

while len(completion) < n:

   
    available = [
        p for p in pros
        if p[1] <= c_time and p[0] not in completion
    ]

    if not available:
        c_time += 1
        continue

    selected = min(available, key=lambda x: x[3])

    pid, at, bt, priority = selected

    if not execution_order or execution_order[-1] != pid:
        execution_order.append(pid)

   
    remain[pid] -= 1
    c_time += 1

    if remain[pid] == 0:
        completion[pid] = c_time

results = []

for p in pros:

    pid, at, bt, priority = p

    ct = completion[pid]
    tat = ct - at
    wt = tat - bt

    results.append([pid, at, bt, priority, ct, tat, wt])

print("\nPriority Scheduling : Preemptive ")

print(
    f"{'PID':<8}"
    f"{'AT':<8}"
    f"{'BT':<8}"
    f"{'Priority':<10}"
    f"{'CT':<8}"
    f"{'TAT':<8}"
    f"{'WT':<8}"
)

for r in results:
    print(
        f"{r[0]:<8}"
        f"{r[1]:<8}"
        f"{r[2]:<8}"
        f"{r[3]:<10}"
        f"{r[4]:<8}"
        f"{r[5]:<8}"
        f"{r[6]:<8}"
    )

Avg_tat = sum(r[5] for r in results) / n
Avg_wt = sum(r[6] for r in results) / n

print(f"Average TAT = {Avg_tat:.2f}")
print(f"Average WT  = {Avg_wt:.2f}")

print("\nPreemtive Priority Scheduling Execution Order:")
print(" -> ".join(execution_order), "-> Done")


print("Non-Pre-emptive Priority Scheduling VS Pre-emptive Priority Scheduling:")
print("Operation\t\tAverage TAT\tAverage WT")

print(
    f"Non-Pre-emptive PS\t"
    f"{avg_tat:.2f}\t\t"
    f"{avg_wt:.2f}"
)

print(
    f"Pre-emptive PS\t\t"
    f"{Avg_tat:.2f}\t\t"
    f"{Avg_wt:.2f}"

)