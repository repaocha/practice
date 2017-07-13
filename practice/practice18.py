#!/usr/bin/python
# -*- coding:UTF-8 -*-

#求s=a+aa+aaa+aaaa+......,其中a是一个数字，几个数相加由键盘控制
Sn=[]
m=0
n=int(raw_input('n:'))
a=int(raw_input('a:'))

for count in range(n):
    m=m+a
    a=a*10
    Sn.append(m)
    print m
    
Sn=reduce(lambda x,y:x+y,Sn)
print "计算和为:",Sn
        