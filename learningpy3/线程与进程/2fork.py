import os
import time
ret = os.fork()
# 使用fork 基础方式如下 os.fork 会分多次返回多个值  就能完成两个while True 一起执行  os.fork 会创建一个新的进程
if ret == 0:
	while True:
		print(1)
		thim.sleep(1)
else:

	while True:
		print(2)
		thim.sleep(1)
