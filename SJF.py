pros = [ 
    ["p1", 3, 2], 
    ["p2", 2, 2], 
    ["p3", 1, 1], 
    ["p4", 1, 2], 
    ["p5", 0, 1], 
    ["p6", 4, 3] 
]

t = 0 
t_TAT = 0 
t_WT = 0 

stores = []
completed = []

n = len(pros)

while len(completed) < n:

   
    available = []

    for i in pros:
        if i[0] not in completed and i[1] <= t:
            available.append(i)

    if len(available) == 0:
        t = min(i[1] for i in pros if i[0] not in completed)
        continue

    available.sort(key=lambda x: (x[2], x[1]))

    pid, at, bt = available[0]

    ct = t + bt
    tat = ct - at
    wt = tat - bt

    t_TAT += tat
    t_WT += wt

    stores.append([pid, at, bt, ct, tat, wt])

    t = ct
    completed.append(pid)


print("Average TAT =", t_TAT / n)
print("Average WT =", t_WT / n)

stores.sort(key=lambda x: int(x[0][1:]))

print("\np_id\tAT\tBT\tCT\tTAT\tWT")

for i in stores:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")

print("Average TAT =", t_TAT / n)
print("Average WT =", t_WT / n)


print("\nThe SJF Serial:")

stores.sort(key=lambda x: x[3])

for i in stores:
    print(i[0], end=" -> ")

print("Done")