#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��дһ������������nΪż��ʱ�����ú�����1/2+1/4+....+1/n,�����nΪ����ʱ�����ú���1/1+1/3+...1/n.

def yang(n):
    i=0
    s=0.0
    for i in range(2,n+1,2):
        s+=1.0/i
    return s
def chen(n):
    s=0.0
    for i in range(1,n+1,2):
        s+=1.0/i
    return s 
def yangchen(fp,n):
    s=fp(n)
    return s
if __name__=='__main__':
    n=int(raw_input('����һ������:'))   
    if n % 2==0:
        sum=yangchen(yang,n)
    else:
        sum=yangchen(chen,n)
    print sum