#!/usr/bin/python
# -*- coding:utf-8 -*-

#�˽���ת����ʮ���ơ�

m=0
n=raw_input('������һ���˽�����:')
for i in range(len(n)):
    m=m*8+ord(n[i])-ord('0')
print m