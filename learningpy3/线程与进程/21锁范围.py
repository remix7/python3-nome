from threading import Thread, Lock
import time
# 锁范围真的是越小越好哦
g_num = 0

def test1():
	global g_num
	for i in range(1000000):
		mutex.acquire()
		g_num += 1
		mutex.release()
	
	print(" test 1 g_num is %d"%g_num)

def test2():
	global g_num
	for i in range(1000000):
		mutex.acquire()#上锁
		g_num += 1
		mutex.release() # 解锁 
	print(" test 2 g_num is %d"%g_num)

print(time.time())


mutex = Lock() #创建一把互斥锁 默认为打开的状态
# test1 和 test2 都在抢着对这个锁进行上锁 如果又一方成功上锁 那么导致
# 另一方在等待到这个锁被解开位置

p1 = Thread(target=test1)
p1.start()

#time.sleep(3)

p2 = Thread(target=test2)
p2.start()

print(time.time())
