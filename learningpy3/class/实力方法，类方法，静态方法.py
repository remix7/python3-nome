#coding=utf-8
#

class Game(object):
	num = 0

	def __init__(self):
		self.name='what'

	@classmethod
	def add_num(cls):
		cls.num = 100

game = Game()
game.add_num()
print(Game.num)