 coding = utf-8

class Person(object):
	def __init__(self,name):
		self.name = name

p1 = Person("laowang")

import types

def run(self):
	print("run name:%s"%self.name)

p1.run = types.MethodType(run,p1)
# types.MethodType 参数为方法名  对象名  可以动态的将方法添加到对象中
# 如果不这样使用的话
# 理论上 p1.run = run 是可以将方法绑定到对象上的
# 可是 这样并不会将p1对象当作第一个参数传递给run方法 所以不行
p1.run()

def eat(self):
	print("eat name:%s"%self.name)

p1.eat = types.MethodType(eat,p1)

p1.eat()

def sport(self):
	print("sport name:%s"%self.name)

p1.sport = sport
p1.sport(p1)

xxx = types.MethodType(sport,p1)

xxx()
# 绑定静态方法
@staticmethod
def test():
	print("static method")
Person.test = test
Person.test()
#添加类方法
@classmethod
def printNum(cls):
	print("class methond")

Person.printNum = printNum
Person.printNum()
# 添加完 对象可以直接调用噢
p1.printNum()

