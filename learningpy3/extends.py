# coding = utf-8

class Parent():
	attr = 100
	"""docstring for Parent"""
	def __init__(self):
		print('parent init')
	def getAttr(self):
		print("attr is",self.attr)
	def setAttr(self,attr):
		self.attr = attr
		print('set attr success')
	def sayHello(self):
		print("parent say hello")


class Child(Parent):
	def __init__(self):
		Parent()
		print('child init')

	def sayHello(self):
		print('child say hello')