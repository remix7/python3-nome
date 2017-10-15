#coding = utf-8

def w1(func):
	def inner():

		print("this is secuityOB")
		func()
	return inner

@w1
def f1():
	
	print("---f1---")

@w1
def f2():
	print("f2")

#第一种用法
#f1 = w1(f1)

f1()
f2()
