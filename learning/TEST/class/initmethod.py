#coding=utf-8

class Cat:


	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return "%s的年龄是：%d"%(self.name,self.age)

	def eat(self):
		print("eat")

	def drink(self):
		print("drink")

	def introduce(self):
		print(self.name)
		print(self.age)
tom = Cat('what',10)
print(tom)