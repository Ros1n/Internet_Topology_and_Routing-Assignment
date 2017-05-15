with open('log_all.txt') as file:
	data = file.readlines()

ip_dict = {}
ip_cur = ''
ip_start = 'Ping statistics for '
for line in data:
	if ip_start in line:
		ip_addr = line[20:len(line)-2]
		ip_cur = ip_addr
		if ip_addr not in ip_dict:
			ip_dict[ip_addr] = ''
	else:
		if 'Minimum =' in line:
			ip_dict[ip_cur] += line.strip().strip(',\'\n') + ','

f = open('max_min_avg.txt', 'w')
for key, val in ip_dict.items():
	#print('key= '+key+' val= ',end='')
	print(val)
	print()
	f.write(val)
	f.write('\n')


