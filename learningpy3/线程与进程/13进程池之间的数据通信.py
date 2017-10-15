from multiprocessing import Manager, Pool
import os, time, random

def reader(q):
	print("reader %s parent pid is %s"%(os.getpid(),os.getppid()))

	for i in range(q.qsize()):
		print("reader queue %s"%q.get(True))

def writh(q):
	
	print("writh %s parent pid is %s"%(os.getpid(),os.getppid()))

	for i in 'taoge':
		q.put(i)

if __name__ == '__main__':
	print(" %s start"%os.getpid())
	
	q = Manager().Queue()

	po = Pool()

	po.apply(writh,(q,))

	po.apply(reader,(q,))
	po.close()
	po.join()
	print("end pid is %s"%os.getpid())


