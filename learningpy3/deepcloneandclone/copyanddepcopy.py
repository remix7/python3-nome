
#coding = utf-8
# 列表与元祖的深浅拷贝
a = [1,2,3]
b = [2,3,4]
c = [a,b]
import copy
e = copy.deepcopy(c)
print(id(c))
print(id(e))
print(id(c[0]))
print(id(e[0]))

# 列表和元祖的深拷贝一样  都是递归深拷贝

f = copy.copy(c)
print(id(c))
print(id(f))
print(id(c[0]))
print(id(f[0]))
# copy.copy 只是第一层深拷贝  并没有递归深拷贝
#如果是元祖使用copy.copy 则只进行浅拷贝
#拷贝要看数据类型是否可变 若不可变则 coyp.copy 只进行浅拷贝·
