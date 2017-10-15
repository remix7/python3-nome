# 带有参数的装饰器
# 先执行带有参数的那个函数 
#获取返回值为装饰器的引用
# 使用返回值对目标函数进行装
def funcargs(pre = 'hello'):


	def func(fn):
		print(pre)
		def func_in(*args,**kwargs):
			print(pre)
			return fn(*args,**kwargs)
		return func_in
	return func
@funcargs("hahha")
def test():
	print(123)

test()
