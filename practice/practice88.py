#!/usr/bin/python
# -*- coding:utf-8 -*-

#��ȡ7������1-50��������ֵ��ÿ��ȡһ��ֵ�������ӡ����ֵ������*��

n=1
while n <=7:
    a=int(raw_input('������һ����:'))
    if a<1 or a>50:
          print 'WRONG!'
    else:
          print a*'*'
    n+=1