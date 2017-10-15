# coding= utf-8
from multiprocessing import Process
import time
import os
class Process_class(Process):
	# 因为Process本身有INIt方法 这个子类相当与重写了这个方法
	# 这样做会带来一个问题 我们并没有真正的去实例化一个Proess
	# 最好的方法是讲集成类本身传递给Process.__init__(self) 完成初始化操作
	def __init__(self,interval):
		Process.__init__(self)
		self.interval = interval
	# 重写了父类的run方法
	
	def run(self):
		print("子进程 %s 开始执行，父进程为 %s"%(os.getpid(),os.getppid()))
		t_start = time.time()
		time.sleep(self.interval)
		t_stop = time.time()

		print(" %s 执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))


if __name__ == "__main__":
	t_start = time.time();
	print("当前进程 %s"%os.getpid())

	p1 = Process_class(2)
	p1.start()
	p1.join()
	t_stop = time.time()
	print(" %s 执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))
