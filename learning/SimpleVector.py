from math import hypot


# 定义向量类
class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 重写字符串构造方法
    # def __repr__(self):
    #     return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # 去绝对值
    def __abs__(self):
        return hypot(self.x, self.y)

    # 判断对象是否为false
    def __bool__(self):
        return bool(self.x or self.y)

    # 向量相加
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 向量相乘
    def __mul__(self, scaler):
        return Vector(self.x * scaler, self.y * scaler)


a = Vector(2, 4)
b = Vector(2, 1)

print(a)
print(b)
print(a + b)
