#FCFS

request_sequence = [3, 4, 60, 21, 2, 10, 11]

head = 10
total = 0
current = head

print("Seqeunce: ")
for i in request_sequence:
    total += abs(current - i)
    current = i
    print(current,end=" ")

print("\nhead Move: ", total)
#Shortest seek Time First
request_sequence = [3, 4, 60, 21, 2, 10, 11]

head = 10
total = 0
current = head
request_sequence.sort()

print("SSTF sequence: ")
while request_sequence:
  x=min(request_sequence, key= lambda i: abs(head-i))
  total += abs(head - x)
  head = x
  request_sequence.remove(x)
  print(head, end=" ")


print("\nhead Move: ", total)
