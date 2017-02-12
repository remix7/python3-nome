class myClass1:
    """A simple example class"""

    def __init__(self):  # 构造函数
        self.data = []

    i = 12345  # 普通成员属性

    def f(self):  # 普通成员函数
        return 'what fuck'

    class A:
        pass


class myClass2:
    def __init__(self, r, i):
        self.r = r
        self.i = i


x = myClass1()
print(x.f())
