#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��һ��������5λ��������Ҫ��:�����Ǽ�λ���������ӡ����λ���֡�

x=int(raw_input('������һ������'))
a=x/10000
b=x%10000/1000
c=x%1000/100
d=x%100/10
e=x%10

if a!=0:
    print "5λ��:",e,d,c,b,a
elif b != 0:
    print "4 λ����",e,d,c,b,
elif c != 0:
    print "3 λ����",e,d,c
elif d != 0:
    print "2 λ����",e,d
else:
    print "1 λ����",e