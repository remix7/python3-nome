# coding=utf-8

import os

# 获取要重命名文件夹的名字
folder_name = input("请输入要重命名的文件夹:")
# 获取指定文件夹中的所有文件的 文件名
filesNameList = os.listdir(folder_name)

os.chdir(folder_name)
# 重命名
for fileName in filesNameList:
	print(fileName)
	os.rename(fileName,"[涛哥出品]-"+fileName)

