#!/usr/bin/python
# -*- coding:UTF-8 -*-

#���õݹ麯�����÷�ʽ�����������5���ַ������෴��˳���ӡ������

def output(s,l):
    if l==0:
       return
    print (s[l-1])
    output(s,l-1)
    
s=raw_input('������һ���ַ�:')
l=len(s)
output(s,l)