生成器
	a = [x << 1 for x in range(10)] 生成一个列表
		如果要生产一个很大的列表而不只使用其中一部分 这样会浪费内存
	g = (x << 1 for x in range(10)
		这是生成器的第一种创建方法
		next(b) 每次执行都会重生成器中获取一个值 而且是有顺序的
		如果next(b)最后一个元素已经取出  再执行会报错
		第二中方式  yield关键字
		例子：
		def createNum():
			a,b = 0,1
			for i in range(5):
				yield b
				a,b = b ,a + b
		加上了yield  这个就不是普通的函数了  而是一个生成器


迭代器
闭包
装饰器

