#!/usr/bin/python
# -*- coding:UTF-8 -*-
from _ast import Num

#ѧϰʹ��auto����������÷���

num=2
def autofunc():
    num=1
    print 'internal block num=%d' % num
    num+=1
for i in range(4):
    print 'The num=%d' % num
    num+=1
    autofunc()