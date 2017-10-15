# coding=utf-8
# 通用类装饰器
class Test(object):
	def __init__(self,func):
		print("init")
		print("func name is %s"%func.__name__)
		self.__func = func
	def __call__(self,*args,**kwargs):
		print("lei zhuangshiqi run")
		return self.__func(*args,**kwargs)


@Test # 这句话相当于  test = Test(test)  然后在执行 test()
def test1():
	print("没有参数和返回值")
test1()
@Test
def test2(a):
	print("有参数无返回值 a = %d"%a)

test2(100)

@Test
def test3():
	print("没有参数有返回值")
	return "hhh"

t = test3()
print(t)

@Test
def test4(a,b):
	print("有参数有返回值 a = %d,b = %d"%(a,b))
	return "12345"
t2 = test4(10,20)
print(t2)
	

