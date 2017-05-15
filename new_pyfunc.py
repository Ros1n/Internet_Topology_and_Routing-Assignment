#import sth

with open('trace.txt') as file:
	data = file.readlines()

#initialise variables
sender_host = set()
receiver_host = set()
source_port = set()
des_port = set()
packet_size = 0
for line in data:
	line2 = line.split()
	sender_host.add(int(line2[1]))
	receiver_host.add(int(line2[2]))
	source_port.add(int(line2[3]))
	des_port.add(int(line2[4]))
	packet_size += int(line2[5])

print('sender host = '+str(len(sender_host)))
print('reciver hsot = '+ str(len(receiver_host)))
print('source port = ' + str(len(source_port)))
print('destination port = ' + str(len(des_port)))
print('total packet size = ' + str(packet_size))