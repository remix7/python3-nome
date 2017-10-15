from threading import Thread
import time


def test1():
	g_num = 100
	g_num += 1
	
	print(" test 1 g_num is %d"%g_num)

def test2():
	g_num = 1

	print(" test 2 g_num is %d"%g_num)

p1 = Thread(target=test1)
p1.start()

#time.sleep(3)

p2 = Thread(target=test2)
p2.start()
