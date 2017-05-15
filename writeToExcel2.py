import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('a sheet')
with open('packet count versus sec.txt') as file:
	lines = file.readlines()
#data = file.read()
i = 1
print('start reading')
sheet.write(0, 0, 'time')
sheet.write(0, 1, 'packet count')
for line in lines:
	#print(line)
	line = line.split()
	packet_count = line[1]
	sec = line[0]
	sheet.write(i, 0, int(sec))
	sheet.write(i, 1, int(packet_count))
	i += 1

book.save('packet_count_versus_sec.xls')

