distance = [14209.77, 10437.78, 8959.52, 11581.72, 18580.34, 17766.56, 13402.11, 2158.32, 9583.26, 14054.82, 12285.36, 16760.07, 16246.46, 18398.15, 13852.65]
speed = [0.29618, 0.36255, 0.16227, 0.472, 0.3891, 0.21518, 0.30818, 0.04755, 0.32873, 0.29936, 0.32864, 0.35509, 0.27373, 0.31255, 0.36164]
for i in range(15):
	#speed = (2*distance[i]*1000)/(3*10**8)
	final = speed[i]/((2*distance[i]*1000)/(3*10**8))
	print(str(final))
	