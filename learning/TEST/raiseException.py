class ShortInputException(Exception):
	def __init__(self,first,last):
		self.first = first
		self.last = last
def  main():
	try:
		s = "an"
		if len(s) < 3:
			raise ShortInputException(len(s),3)
	except ShortInputException as res :
		print(res)
	else:
		print("no exception")
main()