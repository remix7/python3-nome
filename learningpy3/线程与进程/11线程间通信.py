# 线程间通讯 Queue

from multiprocessing import Queue

q = Queue(3)

q.put("what")

print(q.full())

q.put("fuck")

q.put("are")

print(q.full())

q.get()

q.get_nowait()

q.qsize()

q.put("h1")

q.put_nowait("123")
