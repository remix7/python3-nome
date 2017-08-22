# coding = utr-8
# 

class Employee(object):
	"""docstring for Employee"""
	def __init__(self, name , pay):
		self.name = name 
		self.pay = pay

	def hello(self):
		'''
		say hello
		'''	
		print(self.name) 
		print('say hello')
