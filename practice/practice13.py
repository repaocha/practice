#!/usr/bin/python
# -*- coding:UTF-8 -*-

#打印出所有的水仙花数，所谓水仙花数是指一个三位数，其各位数立方和等于
#该数，其各位数立方和等于该数本身。
for n in range(100,1000):
    i=n/100
    j=n/10 %10
    k=n % 10
    if n==i*i*i+j*j*j+k*k*k:
     print n