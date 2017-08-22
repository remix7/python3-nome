#coding=utf-8
# 深拷贝
import copy
a = [11,22]
b = copy.deepcopy(a)
print(id(a))
print(id(b))
