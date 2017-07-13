#!/usr/bin/python
# -*- coding:UTF-8 -*-

#给一个不多于5位的整数，要求:求它是几位数，逆序打印出各位数字。

x=int(raw_input('请输入一个数：'))
a=x/10000
b=x%10000/1000
c=x%1000/100
d=x%100/10
e=x%10

if a!=0:
    print "5位数:",e,d,c,b,a
elif b != 0:
    print "4 位数：",e,d,c,b,
elif c != 0:
    print "3 位数：",e,d,c
elif d != 0:
    print "2 位数：",e,d
else:
    print "1 位数：",e