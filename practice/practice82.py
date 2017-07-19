#!/usr/bin/python
# -*- coding:utf-8 -*-

#八进制转换成十进制。

m=0
n=raw_input('请输入一个八进制数:')
for i in range(len(n)):
    m=m*8+ord(n[i])-ord('0')
print m