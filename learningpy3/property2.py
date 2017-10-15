# coding = utf-8
class Test(object):
	
	def __init__(self):
		self.__num = 100

	@property
	def num(self):
		print("getter")
		return self.__num
	
	@num.setter
	def num(self,value):
		print("setter")
		self.__num = value


t = Test();
print(t.num)
t.num = 300
print(t.num)


