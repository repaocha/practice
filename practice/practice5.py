#!/usr/bin/python
# -*-coding:UTF-8 -*-

#输入三个整数x,y,z,请把这三个数从小到大输出。

x=int(raw_input('整数integer:'))
y=int(raw_input('整数integer:'))
z=int(raw_input('整数integer:'))

l=[x,y,z]
l.sort()
print '这三个数由小到大的顺序:',l
n=[x,y,z]
n.sort(reverse=True)
print '这三个数由大到小的顺序:',n