# coding=utf-8

class Cat:

	def eat(self):
		print(self)
		print("猫在吃鱼。。。")


	def drink(self):
		print("猫在喝可乐。。。 self")

	def introduce(self):
		print("%s的年龄是：%d"%(self.name,self.age))
tom = Cat()
tom.eat()
tom.drink()
tom.name='what fuck'
tom.age=40
tom.introduce()