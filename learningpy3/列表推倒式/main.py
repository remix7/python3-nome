#coding = utf-8
#生成一个列表

a = [i for i in range(10,77)]
print(a)

a = [i for i in range(100) if i%2 == 0]
print(a)

b = [(i,j) for i in range(10) for j in range(3)]
print(b)
