#!/usr/bin/python
# -*- coding:utf-8 -*-

#输入一个正整数，然后判断最少几个9除以该数的结果为整数。

a=int(raw_input('请输入一个整数：'))
x=9
y=1

while(1):
    if x%a==0:
        break
    else:
        x=x*10+9
        y+=1
print '%d个9除以%d为整数,这个数为:%d' % (y,a,x)