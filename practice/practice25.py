#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��1+2!+3!+...�ĺ͡�

n=0
sum=0
t=1
for n in range(1,21):
    t*=n
    sum+=t
print sum