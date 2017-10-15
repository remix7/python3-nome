from threading import Thread,Lock
from time import sleep
class Task1(Thread):
	def run(self):
		while True:
			if lock1.acquire():
				print("task 1")
				sleep(0.3)
				lock2.release()


class Task2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print("task 2")
				sleep(0.3)
				lock3.release()
class Task3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print("task 3")
				sleep(0.3)
				lock1.release()

lock1 = Lock()
lock2 = Lock()
lock2.acquire()
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()
