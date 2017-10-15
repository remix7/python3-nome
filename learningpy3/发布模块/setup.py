#coding=utf-8
'''
发布模块的一般步骤：
1.在包同级目录新建setup.py 添加如下内容
2.执行python setup.py build
3.build后会产生一个build目录 到这个目录里面 python setup.py sdist 即可打包
'''
from distutils.core import setup

setup(
	name="taoge",
	version="1.0",
	description="taoge module",
	author="taoge",
	py_modules=['TestMsg.sendmsg','TestMsg.recvemsg']
)
