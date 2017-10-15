from multiprocessing import Process,Queue

import os, time, random

def writh(q):
	for value in ['a','b','c']:
		print("value is %s"%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			value = q.get()
			print("get value is %s"%value)
			time.sleep(random.random())
		else:
			break

if __name__ == '__main__':
	q = Queue()

	pw = Process(target=writh,args=(q,))

	pr = Process(target=read,args=(q,))

	pw.start()
	
	pw.join()

	pr.start()

	pr.join()
