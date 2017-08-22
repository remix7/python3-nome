#coding=utf-8
#
class Test(object):

	def __init__(self,switch):
		self.switch = switch

	def calc(self,a,b):
		try:
			return a/b
		except Exception as res:
			if self.switch:
				print("hhh")
				print(res)
			else:
				print("what fuck")
				raise

a = Test(True)
a.calc(11,0)
a.switch = False
a.calc(10,0)