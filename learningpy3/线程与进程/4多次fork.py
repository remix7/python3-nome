import os
import time
ret = os.fork()
# 使用fork 基础方式如下 os.fork 会分多次返回多个值  就能完成两个while True 一起执行  os.fork 会创建一个新的进程
# 父进程
if ret == 0:
	print(1)
else:
	# 子进程
	print(2)
# 父进程 子进程
ret = os.fork()
if ret == 0:
	# 父 子
	print(1)
else:
	# 父 子
	print(2)

# 刚开始两个进程  程序执行完成后有四个进程
# 因为第一个进程执行结束后 会再进程中继续往下执行 遇到fork会再次生成新的进程来执行哦
