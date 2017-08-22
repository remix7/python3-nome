# 通用装饰器 返回值 参数都不怕噢

def func(fn):
	def func_in(*args,**kwargs):
		return fn(*args,**kwargs)
	return func_in

@func
def test():
	pass

test()

@func
def test2(a,b):
	print("a = %d b = %d"%(a,b))

test2(1,2)

@func
def test3():
	return "hahah"

print(test3())

@func
def test4(a):
	return a
print(test4("abc"))
