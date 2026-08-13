pros = [
    ["p1", 3, 2],
    ["p2", 2, 2],
    ["p3", 1, 1],
    ["p4", 1, 2],
    ["p5", 0, 1],
    ["p6", 4, 3]
]


pros.sort(key=lambda x: x[1])

t = 0
t_TAT = 0
t_WT = 0

stores = []

for i in pros:
    pid, at, bt = i

    if t < at:
        t = at

    ct = t + bt
    tat = ct - at
    wt = tat - bt

    t_TAT += tat
    t_WT += wt

  
    stores.append([pid, at, bt, ct, tat, wt])

    t = ct

n = len(pros)

print("Average TAT =", t_TAT / n)
print("Average WT =", t_WT / n)


stores.sort(key=lambda x: int(x[0][1:]))

print("\np_id\tAT\tBT\tCT\tTAT\tWT")

for i in stores:
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
print("Average TAT =", t_TAT / n)
print("Average WT =", t_WT / n)

print("\nThe FCFS Serial:")
for i in pros:
    print(i[0], end=" -> ")

print("Done")