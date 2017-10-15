def createNum():
	#print(1)
	a,b = 0,1
	for i in range(10):
		#print(2)
		yield b
		#print(3)
		a,b = b,a+b
		#print(4)


for num in createNum():
	print(num,end=" ")


