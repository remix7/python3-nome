#coding = utf-8

def test(number):

	print(1)
	def test_in():
		print(2)
		print(number + 100)
	
	print(3)
	return test_in

ret = test(100)
ret()
