import statistics
list1 = []

def category_rtt(line):
	minimum_list = []
	maximum_list = []
	avg_list = []
	line = line.split(',')
	for e in line:
		if 'Minimum =' in e:
			minimum_list.append(int(e[10:len(e)-2]))
		elif 'Maximum =' in e:
			maximum_list.append(int(e[10:len(e)-2]))
		elif 'Average =' in e:
			avg_list.append(int(e[10:len(e)-2]))
		else:
			pass
	max1 = round(sum(maximum_list)/len(maximum_list),2)
	min1 = round(sum(minimum_list)/len(minimum_list),2)
	avg1 = round(sum(avg_list)/len(avg_list),2)
	std = round(statistics.stdev(avg_list), 2)
	return min1, max1, avg1, std



with open('max_min_avg.txt') as file:
	data = file.readlines()


for line in data:
	if len(line) > 0:
		tuple1 = category_rtt(line)
		list1.append(tuple1)

i = 0
for a in list1:
	print(str(i) + ':',end='')
	print(a)
	i += 1
		



#print('avg max= '+str(sum(maximum_list)/len(maximum_list)))
#print('avg min= '+ str(sum(minimum_list)/len(minimum_list)))
#print('avg avg= '+ str(sum(avg_list)/len(avg_list)))
