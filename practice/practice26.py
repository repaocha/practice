#!/usr/bin/python
# -*- coding:UTF-8 -*-

#利用递归方法求5！

def yang(i):
    if i==0:
        return 1
    else:
        return i*yang(i-1)
print yang(5)

def chen(i):
     sum=0
     if i==0:
        sum=1
     else:
        sum=i*chen(i-1)
     return sum

for j in range(6):
    print '%s!=%s' % (j,chen(j))