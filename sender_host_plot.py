import time

file = open('trace.txt')
i = 0
total_time = 0
total_bits = 0
sender_hop = {}
for line in file:
    list_line = line.split()
    sender = int(list_line[1])
    if sender in sender_hop.keys():
        sender_hop[sender] += 1
    else:
        sender_hop[sender] = 1

for key, val in sender_hop.items():
    print(key, end=', ')
    print(val)
