import time

file = open('trace.txt')
i = 0
total_time = 0
total_bits = 0
sender_hop = set()
receiver_hop = set()
source_port = set()
des_port = set()
for line in file:
    list_line = line.split()
    #print(line)
    #timestamp = line.split()[0]
    #total_time += float(timestamp)
    #bits = line.split()[5]
    #total_bits += float(bits)
    sender_hop.add(list_line[1])
    receiver_hop.add(list_line[2])
    source_port.add(list_line[3])
    des_port.add(list_line[4])
'''
s = source_port.difference(des_port)
d = des_port.difference(source_port)
'''
print('source port: ')
print(len(sender_hop))
print('destination port: ')
print(len(des_port))


#print(total_bits)
#print(total_time)
print('sender hop: ')
print(len(sender_hop))
print()
print()
print('receiver hop: ')
print(len(receiver_hop))
s = sender_hop.difference(receiver_hop)
print('final sender hop: ')
print(len(s))    
print('final reciver hop: ')
r = receiver_hop.difference(sender_hop)
print(len(r))
