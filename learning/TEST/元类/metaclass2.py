#coding=utf-8

#__metaclass__ 属性标识着 类在创建对象时 由这个属性的值创建
#一般有python解释器自动创建
# py3
def upper_attr(future_class_name,future_class_parents,future_class_attr):
	newAttr = {}
	for name,value in future_class_attr.items():
		if not name.startswith("__"):
			newAttr[name.upper()] = value

	return type(future_class_name,future_class_parents,newAttr)

class Foo(object,metaclass=upper_attr):
	#__metaclass__ = upper_attr #设置Foo类的元类为upper_attr
	bar = 'bip'

print(hasattr(Foo,"bar"))
print(hasattr(Foo,"BAR"))

f = Foo()
print(f.BAR)

