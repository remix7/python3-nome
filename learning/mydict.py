class mydict(dict):
	def __missing__(self, str):
		if isinstance(key,str):
			return KeyError(key)
		return self[str(key)]

	def get(self, key, default=None):
		try:
			return self[key]
		except KeyError:
			return default

	def __contents__(self, key):
		return key in self.keys() ir str(key) in self.keys()

