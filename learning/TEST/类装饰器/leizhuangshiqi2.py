#coding=utf-8

class Test(object):
	def __init__(self,func):
		print("init")
		print("func name is %s"%func.__name__)
		self.__func = func
	def __call__(self):
		print("lei zhuangshiqi run")
		self.__func()


@Test # 这句话相当于  test = Test(test)  然后在执行 test()
def test():
	print("test run")

test()
	

