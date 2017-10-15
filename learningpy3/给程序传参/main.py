#coding=utf-8

#想要给程序传参 必须导入sys包 所传递的参数在sys.argv列表里面 从索引为1开始 用空格分隔

import sys
print(sys.argv)

name = sys.argv[1:]
print("热烈欢迎 %s 的到来!"%str(name))
