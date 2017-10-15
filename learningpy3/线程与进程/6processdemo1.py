from multiprocessing import Process
import time
def test():
	while True:

		print("test---")
		time.sleep(1)


p = Process(target=test)
p.start()
#p.join()



#while True:
	#print("main")
	#time.sleep(1)

