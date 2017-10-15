import gevent

def f(n):
	for i in range(n):
		print("gevent -> %s , i -> %d"%(gevent.getcurrent(),i))
		# 用来模拟一个耗时操作 不是time模块中的sleep
		gevent.sleep(0.5)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,6)
g3 = gevent.spawn(f,7)

g1.join()
g2.join()
g3.join()