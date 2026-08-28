#FCFS Implementation

pros =[
    ["p0", 0, 4],
    ["p1", 1, 3],
    ["p2", 2, 1],
    ["p3", 3, 5]

]

pros.sort(key=lambda x: x[1])

t= 0
t_TAT = 0
t_WT= 0

stores= []

for i in pros:
    pid, at, bt = i

    if t < at:
        t= at

    ct = t + bt
    tat = ct - at
    wt = tat - bt

    t_TAT += tat
    t_WT += wt

    stores.append([pid, at, bt, ct, tat, wt])

    t= ct

n = len(pros)

stores.sort(key=lambda x: int(x[0][1:]))

print(" \n|| FCFS ||")

print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for i in stores:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
print("Average TAT =", t_TAT / n)
print("Average WT =", t_WT / n)

print("The FCFS Serial:")
for i in pros:
    print(i[0], end=" -> ")

print("Done")

#Round Robin Implemetation

pros = [
    ["P0", 0, 4],
    ["P1", 1, 3],
    ["P2", 2, 1],
    ["P3", 3, 5]
]

time_quantum = 2

remain= {p[0]: p[2] for p in pros}
comp = {}
queue= []
visited = set()
time = 0
execution= []

while len(comp)< len(pros):

    for p in pros:
        pid,at,bt = p

        if at <= time and pid not in visited and pid not in comp:
            queue.append(pid)
            visited.add(pid)

    if not queue:
        time += 1
        continue

    pid= queue.pop(0)
    
    run_time= min(time_quantum, remain[pid])

    execution.append((pid, time, time + run_time))
    time += run_time
    remain[pid]-= run_time

    for p in pros:
        if p[1] <= time and p[0] not in visited and p[0] not in comp:
            queue.append(p[0])
            visited.add(p[0])

    if remain[pid]> 0:
        queue.append(pid)
    else:
        comp[pid] = time

total_tat= 0
total_wt = 0
print(" \n|| ROUND ROBIN ||\n")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for pid, at, bt in pros:
    ct = comp[pid]
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")


print("\nThe Round Robin Serial:")
for pid, start, end in execution:
    print(f"{pid} ({start}-{end})", end=" -> ")

print("Done")

print("\nAverage Turnaround Time:",
      total_tat / len(pros))

print("Average Waiting Time:",
      total_wt / len(pros))


print("FCFS VS ROUND ROBIN:")
print("Operation\tAverage TAT\tAverage WT")
print(
f"FCFS\t\t"
f"{t_TAT / n:.2f}\t\t"
f"{t_WT/n:.2f}"
)
print(
f"ROUND ROBIN\t"
f"{total_tat / len(pros):.2f}\t\t"
f"{total_wt / len(pros):.2f}"
)
