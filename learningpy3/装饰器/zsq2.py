# coding = utf-8
# 只要python执行到@装饰器已经装饰完成 在调用的时候不会二次装饰：
# 定义函数 完成数据包裹
def makeBold(fn):
	def wrapped():
		print("1")
		return "<b>" + fn() + "</b>"

	return wrapped

#定义汗湿 完成数据包裹
def makeItalic(fn):
	def wrapped():
		print("2")
		return "<i>" + fn() + "</i>"
	return wrapped

@makeBold
@makeItalic
def test3():
	print(3)
	return "hello world"


print(test3())
