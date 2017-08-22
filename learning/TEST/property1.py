# coding = utf-8
class Test(object):
	
	def __init__(self):
		self.__num = 100

	
	def setNum(self,newNum):
		print("setter")
		self.__num = newNum
	
	def getNum(self):
		print("getter")
		return self.__num
	
	num = property(getNum,setNum)


t = Test();
print(t.num)
t.num = 111;
print(t.num)

