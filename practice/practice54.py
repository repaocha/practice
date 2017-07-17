#!/usr/bin/python
# -*- coding:UTF-8 -*-

#取一个整数a从右端开始的4-7位。

if __name__=='__main__':
    a=int(raw_input('input a number；'))
    b=a >>4
    c=~(~0 <<4)
    d=b & c
    print '%s  %s' % (a,d)