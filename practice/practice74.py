#!/usr/bin/python
# -*- coding:UTF-8 -*-

#�б���������,���ӿ���ʹ��a+b����extend()������

a=[1,3,2,4]
b=[5,7,6,8]
a.sort()
b.sort()
print a
print b
print a+b

a.extend(b)
print a
