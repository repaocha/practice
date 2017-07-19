#!/usr/bin/python
# -*- coding:UTF-8 -*-

#反向输出一个链表。

s=[]
for i in range(5):
    a=int(raw_input('请输入一个数字:'))
    s.append(a)

s.reverse()
print s