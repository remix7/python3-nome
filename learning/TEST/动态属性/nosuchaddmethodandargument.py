#coding=utf-8

# python是动态语言 可以加以设置 让其不能动态添加某些属性或方法

class Person(object):
	# 只能添加这里设置过的属
	__slots__ = ("name","age")

p = Person()
p.name = 'laowang'
p.age = 20
p.score = 100
print(p.name)
print(p.age)
print(p.score)
