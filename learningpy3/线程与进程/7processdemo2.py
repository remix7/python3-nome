from multiprocessing import Process
import time

def test():
	for i in range(5):
		print("test")
		time.sleep(1)

#p = Process(target=test)
#p.start()

#while True:
#	print("main")
#	time.sleep(1)

if __name__ == "__main__":
	p = Process(target=test)
	p.start()
	p.join(2) # 等到p标记的进程结束以后再进行以后的操作
	# 起到堵塞进程的作用哦
	# 有一个参数是超时时间  如果超时则继续往下执行哦
	# 同时等待的进程将会继续执行哦
	# p.terminate() 直接讲子进程干死
	print("123")
