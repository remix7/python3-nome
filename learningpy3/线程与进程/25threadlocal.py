import threading
# 使用函数传递参数的方式可以做到 使用全局字典的方式可以做到 使用local线程也可以做到
local_thread = threading.local()

def process_stu():
	std = local_thread.stu
	print('hello %s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
	local_thread.stu = name
	process_stu()

t1 = threading.Thread(target=process_thread,args=('what',),name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('fuck',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()
