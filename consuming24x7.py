#seperate data

with open('196.216.167.71.txt') as file:
	data = file.readlines()
rrt_collection = {}
for line in data:
	line = line.split('.')
	if line and line != '' and line != '\n' and len(line) > 1:
		print(len(line))
		rrt = int(line[len(line)-1])
		#length = len(rrt)/4
		#for i in range(4):
		rrt_collection[rrt] = line[0]

print(sorted(rrt_collection))




	