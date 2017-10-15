#coding=utf-8
# 不定长参数的装饰器
def func(fn):
	print(1)
	def func_in(*args,**kwargs):# 16 如果ab没有定义 会导致最终程序调用失败
		print("in 1")
		fn(*args,**kwargs) # 2如果没有将ab当实参进行传递 则在函数定义调用会失败
		print("in 2")
	
	print(2)
	return func_in

@func
def test(a,b,c):
	print("a = %d  b = %d  c = %d"%(a,b,c))


test(1,2,123)
