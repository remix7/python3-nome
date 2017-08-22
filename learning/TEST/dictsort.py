# coding=utf-8
# 

infos = [{"name":"xiaoming","age":10},{"name":"laowang","age":19},{"name":"zhaosi","age":25}]

infos.sort(key = lambda obj : obj['age']);

print(infos)