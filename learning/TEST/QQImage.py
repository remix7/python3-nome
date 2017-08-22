# coding = utf-8

myPath = './'
fontPath = './'
inputPath = 'photo.jpg'
outputPath = 'out.jpg'

from PIL import Image,ImageFont,ImageDraw
#打开图片
img = Image.open(myPath+inputPath)
draw = ImageDraw.Draw(img)
#根据图片大小确定字体大小
fontSize = min(img.size)/4
#加文字
print(img.size)