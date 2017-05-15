#ohohohohoh

file = open('trace.txt')
sender_hop = set()
receiver_hop = set()
source_port = set()
des_port = set()
time_count = {}
size = []
i = 1
for line in file:
	#print(line)
	line_list = line.split()
	time = float(line_list[0])
	#sender_hop.add(line_list[1])
	#receiver_hop.add(line_list[2])
	#source_port.add(line_list[3])
	#des_port.add(line_list[4])
	print(int(line_list[5]))
	#size.append(int(line_list[5]))


