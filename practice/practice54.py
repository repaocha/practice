#!/usr/bin/python
# -*- coding:UTF-8 -*-

#ȡһ������a���Ҷ˿�ʼ��4-7λ��

if __name__=='__main__':
    a=int(raw_input('input a number��'))
    b=a >>4
    c=~(~0 <<4)
    d=b & c
    print '%s  %s' % (a,d)