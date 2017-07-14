#!/usr/bin/python
# -*- coding:UTF-8 -*-

#有一个已经排好序的数组。现输入一个数，要求按原来的规律将他插入数组中。
x=[1,3,5,7,9,11,13,15,17]
y=int(raw_input('请输入数字:'))
x.append(y)
x.sort()
print x