# coding=utf-8
# 
def getNum(num):
	if num > 1:
		return num * getNum(num-1)
	else:
		return num

print(getNum(30))