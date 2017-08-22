try:
	# open("what.xyz")
	print("hello")
	print(numm)
except FileNotFoundError:
	print("123")
except Exception as res:
	print("what fuck")
	print(res)
else:
	print("没有异常")
finally:
	print("有没有都会执行")