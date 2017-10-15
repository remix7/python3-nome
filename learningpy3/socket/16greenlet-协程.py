# coding = utf-8

from greenlet import greenlet
import time

def t1():
	while True:
		print('--A--')
		gr2.switch()
		time.sleep(0.5)

def t2():
	while True:
		print('--B--')
		gr1.switch()
		time.sleep(0.5)

gr1 = greenlet(t1)
gr2 = greenlet(t2)
gr1.switch()