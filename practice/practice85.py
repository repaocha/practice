#!/usr/bin/python
# -*- coding:utf-8 -*-

#����һ����������Ȼ���ж����ټ���9���Ը����Ľ��Ϊ������

a=int(raw_input('������һ��������'))
x=9
y=1

while(1):
    if x%a==0:
        break
    else:
        x=x*10+9
        y+=1
print '%d��9����%dΪ����,�����Ϊ:%d' % (y,a,x)