#ohohohohoh

file = open('trace.txt')
sender_hop = set()
receiver_hop = set()
source_port = set()
des_port = set()
time_count = {}
size_dict = {}
i = 1
for line in file:
	#print(line)
	line_list = line.split()
	time = float(line_list[0])
	sender_hop.add(line_list[1])
	receiver_hop.add(line_list[2])
	source_port.add(line_list[3])
	des_port.add(line_list[4])
	#size.append(int(line_list[5]))
	size = int(line_list[5])
	if size in size_dict:
		size_dict[size] += 1
	else:
		size_dict[size] = 1

'''
	if time < i:
		if i in time_count.keys():
			time_count[i] += 1
		else:
			time_count[i] = 0
	else:
		i += 1
		time_count[i] = 1

#print(time_count)

for key, val in time_count.items():
	print(str(key) + ' ' + str(val))
'''
for key, val in size_dict.items():
	print(key,end=', ')
	print(val)

#print(size_dict)
