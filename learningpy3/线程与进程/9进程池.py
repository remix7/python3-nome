from multiprocessing import Pool
import os,time,random
# Pool(3) 表示 最多有三个进程一起执行任务
# 如果添加的任务数量多了 并不会导致任务添加不进去
#  添加到进程中的人物 如果还没有执行的话 那么此时 他们会等待进程池中
#  进程完成一个任务后 会自动的去用刚刚那个进程 完成当前的任务
def woker(msg):
	t_start = time.time()
	print("%s start process id is:%d"%(msg,os.getpid()))

	time.sleep(random.random()*2)

	t_stop = time.time()

	print(msg,"stop use time is:%0.2f"%(t_stop-t_start))

if __name__ == '__main__':
	po = Pool(3)

	print("start")
	for i in range(0,10):
		#pool.apply_async(要调用的目标,（传递的参数元祖）,）
		po.apply_async(woker,(i,))
		# 如果为 po.apply() 则为阻塞模式

	# close 相当于不能在向进程池中添加新的任务
	po.close()
	# join相当与主进程等待进程池全部执行完毕 再进行后续执行
	# 如果没有join 则会导致进程池中的任务 在主进程结束的时候被结束
	po.join()

	print("stop")

