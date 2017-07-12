#!/usr/bin/python
#-*- coding:UTF-8 -*-

#输出99乘法口诀表。
for i in range(1,10):
    print
    for j in range(1,i+1):
       print '%s*%s=%s' %(i,j,i*j),