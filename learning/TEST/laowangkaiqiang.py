# coding=utf-8

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
	def pushZidan(self,danjia,zidan):
		danjia,addZidan(zidan)
	def pushDanjia(self,gun,danjia):
		gun.addDanjia(danjia)

class Gun(object):
	"""docstring for Gun"""
	def __init__(self, type):
		super(Gun, self).__init__()
		self.type = type
	def addDanjia(self,danjia):
		self.haveDanjia = True
		
class Danjia(object):
	"""docstring for Danjia"""
	def __init__(self, size):
		super(Danjia, self).__init__()
		self.size = size
	def addZidan(self,zidan):
		self.count += 1

class Zidan(object):
	"""docstring for Zidan"""
	def __init__(self, sha_shang_li):
		super(Zidan, self).__init__()
		self.sha_shang_li = sha_shang_li
		
def main():
	#1 创建老王对象
	laowang = Person("老王")
	#2 创建一个枪对象
	ak47 = Gun("AK47")
	#3 创建一个弹夹对象
	danjia = Danjia(20)
	#4 创建一些子弹
	zidan = Zidan(20)
	#6 老王把子弹安装到弹夹中
	laowang.pushZidan(danjia,zidan)
	#7 老王把弹夹安装到枪中
	laowang.pushDanjia(ak47,danjia)
	#8 老王拿枪
	
	#5 创建一个敌人
	#9 老王开枪打敌人
	pass
if __name__ == '__main__':
	main()