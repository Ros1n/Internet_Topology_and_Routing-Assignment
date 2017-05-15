#ohohohohoh

file = open('trace.txt')
sender_hop = set()
receiver_hop = set()
source_port = set()
des_port = set()
time_count = {}
size_list = []
i = 1
for line in file:
	#print(line)
	line_list = line.split()
	size = int(line_list[5])
	size_list.append(size)

print('shit')
print(sum(size_list))