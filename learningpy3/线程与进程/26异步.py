from multiprocessing import Pool
import time
import os

def test():
	print('进程池中的进程pid = %d ppid = %d'%(os.getpid(),os.getppid()))

	for i in range(3):
		print(i)
		time.sleep(1)
	return 'hhh'

def test2(args):
	print('callback func  pid = %d'%os.getpid())
	print('callback func args = %s'%args)

if __name__ == '__main__':

	pool = Pool(5)
	pool.apply_async(func=test,callback=test2)
	time.sleep(5)

	print('main pid = %d'%os.getpid())
