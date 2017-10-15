import threading
import time

def saySorry():
	print(time.time())
	print("sorry sorry")
	time.sleep(1)

if __name__ == '__main__':
	for i in range(5):
		t = threading.Thread(target=saySorry)
		t.start()
