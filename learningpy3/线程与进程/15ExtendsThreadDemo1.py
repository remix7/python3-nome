# coding = utf-8

import threading
import time

class MyThread(threading.Thread):
	
	def run(self):
		for i in range(5):
			time.sleep(1)

			print(" i'm %s @ %s"%(self.name,str(i)))


if __name__ == '__main__':
	t = MyThread()
	t.start()
