# coding=utf-8

class Test(object):
	pass
t1 = Test()
# 此方法有三个参数 创建的类名 父类元祖 参数kv字典
Test2 = type("Test2",(),{})

t2 = Test2()
print(t2)
# 创建带有属相的类  使用type

Test3 = type("Test3",(),{"num":0})

t3 = Test3();
print(t3.num)

# 创建到带有方法的类  使用type
def printNum(self):
	print("---num is %d---"%self.num)

Test4 = type("Test4",(),{"num":0,"printNum":printNum})
t4 = Test4();
t4.printNum()

# 一个类继承一个类
def eat(self):
	print("---eat----")

Animal = type("Animal",(),{"eat":eat})

Dog = type("Dog",(Animal,),{})

wangcai = Dog();
wangcai.eat()
