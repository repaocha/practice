#!/usr/bin/python
# -*- coding:UTF-8 -*-

#对10个数进行排序。
print '请输入10个数字\n'
a=[]
for n in range(10):
    a.append(int(raw_input('输入1个数字:\n')))
a.sort()
print a    