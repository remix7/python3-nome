#coding=utf-8

def func(fn):
	print(1)
	def func_in(a,b):# 16 如果ab没有定义 会导致最终程序调用失败
		print("in 1")
		fn(a,b) # 2如果没有将ab当实参进行传递 则在函数定义调用会失败
		print("in 2")
	
	print(2)
	return func_in

@func
def test(a,b):
	print("a = %d  b = %d"%(a,b))


test(1,2)
