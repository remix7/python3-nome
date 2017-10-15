l ----> list显示当前代码
n ----> next 向下一行执行
c ----> contrinue 继续执行代码
b ----> break 添加一个断点
clear n(断点序号) 清除一个断
s ----> step 跳到要执行的函数
p ----> print 加参数名  可以看到传递给函数的参数值
a ----> args 查看所有调用函数的参数值
q ----> quit 退出调试
r ----> return 快速执行到代码最后一行

在交互模式下使用pab调试程序

import pdb

prd.run('函数名(参数。。）')

这样即可在交互模式下对程序进行调试
出现pdb界面时 需要按 s进入函试

在程序里埋点调试
import pdb
pdb.set_trace()

在执行时当执行到埋的点就回自动跳入pdb调试模式
