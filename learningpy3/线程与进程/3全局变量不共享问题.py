import os
import time

g_num = 100
# 线程独立执行不共享全局变量  真的不共享哦  真的不共享哦
# 线程独立执行不共享全局变量
# abcdefghijklmnopqrstuvwzyz
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyz
# 线程之间独立执行 不共享全局变量
# 互不影响 相当与分家 各过各的  真的是各过各的哦
# 什么 what fuck 你竟然不相信 
# ret = os.fork()
# 不仅全局变量 线程中几乎什么都不会共享的  
ret = os.fork()

if ret == 0:
	print("this is process 1")
	g_num += 1
	print("g_num = %d"%g_num)
else:
	time.sleep(3)
	print("this is process 2")
	print("g_unm = %d"%g_num)

