#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��һ�������У�2/1,3/2,5/3,8/5,13/8....���������е�ǰ20��֮�͡�

a=2.0
b=1.0
sum=0

for n in range(20):
    sum+=a/b
    a,b=a+b,a
print sum
