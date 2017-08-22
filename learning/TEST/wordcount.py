# coding = utf-8
# 
import re
from collections import Counter
FILESOURCE = './file.py'

def getMostCommonWord(articleFileSource):
 	'''
		输入纯文本文件 统计单词出现的个数
 	'''
 	pattern = r'''[A-Za-z]+|\$\d+%?$'''
 	f = open(articleFileSource,'r')
 	while f:
 		f = re.findall(pattern,f.read())
 		return Counter(f).most_common()

if __name__ == '__main__':
	print(getMostCommonWord(FILESOURCE))
