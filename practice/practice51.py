#!/usr/bin/python
# -*- coding:UTF-8 -*-

#学习使用按位与&

if __name__=='__main__':
    a=077
    b=a & 3
    print 'a & b=%s' % b
    b &=7
    print 'a & b=%s' % b