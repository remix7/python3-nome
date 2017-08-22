# coding=utf-8
# 用一个变量指向 yield 并不是用其获取yield的返回值  而是再调用send方法时可以传递一个参数
# 使用send
def test():
	i = 0
	while i<5:
		temp = yield i
		print(temp)
		i += 1

a = test()
a.send(None) # 注意如果一定要使用send 第一次调用时一定要传递None
#或者在send 之前调用一下__next__ 

