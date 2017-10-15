# coding=utf-8

class CarStore(object):
	
	def __init__(self):
		self.factory = Factory()

	def order(self,carType):
		return self.factory.selectCarByType(carType)

class Factory(object):
	def selectCarByType(self,carType):
		if carType == '名图':
			return Mingtu()
		elif carType == '索纳塔':
			return Suonata()
		elif carType == 'ix35':
			return Ix35()
			
class Car(object):
	def move(self):
		pass
	def music(self):
		pass
	def stop(self):
		pass

class Suonata(Car):
	pass

class Mingtu(Car):
	pass

class Ix35(Car):
	pass

carStore = CarStore()
car = carStore.order('名图')