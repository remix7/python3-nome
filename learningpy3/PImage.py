# coding=utf-8

inputPath = "" #"'D:\\PROJECT\\PYTHON\\TEST\\input\\'
outputPath = "" # 'D:\\PROJECT\\PYTHON\\TEST\\output\\'

from PIL import Image
import os

def processImage(filesource,destsource,name,imgtype):
	imgtype = 'jpeg' if imgtype == '.jpg' else '.png'
	print(filesource+name)
	print(name)
	print(destsource)
	print(imgtype)
	im = Image.open(filesource + name)
	print(im)
	rate = max(im.size[1]/1080.0 if im.size[1] > 1080 else 0,im.size[0]/1920.0 if im.size[0] > 1920 else 0)
	if rate:
		im.thumbnail((im.size[0]/rate,im.size[1]/rate))
	im.save(destsource+name,imgtype)

def run():
	os.chdir(inputPath)
	for i in os.listdir(os.getcwd()):
		postfix = os.path.splitext(i)[1]
		if postfix == '.jpg' or postfix == '.png':
			print(os.getcwd())
			processImage(inputPath,outputPath,i,postfix)


if __name__ == '__main__':
	run()