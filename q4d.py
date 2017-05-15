import collections

file = open('trace.txt')
sender_hop = {}
receiver_hop = set()
source_port = set()
des_port = set()
time_count = {}
size = []
i = 1
for line in file:
	#print(line)
	line_list = line.split()
	#time = float(line_list[0])
	#sender_hop.add(line_list[1])
	#receiver_hop.add(line_list[2])
	#source_port.add(line_list[3])
	#des_port.add(line_list[4])
	#size.append(line_list[5])
	hop = int(line_list[1])
	if hop in sender_hop:
		sender_hop[hop] += 1
	else:
		sender_hop[hop] = 1
#od = collections.OrderedDict(sorted(sender_hop.items()))
c = 1
for w in sorted(sender_hop, key=sender_hop.get, reverse=True):
	print(c, end=', ')
	print(sender_hop[w])
	#print(w)
	c += 1


