#!/usr/bin/python
# -*- coding:utf-8 -*-

#某个公司采用公用电话传递数据，数据是四位的整数，在传递的过程中是加密的，加密规则如下：每个数字都加上5，然后用和除以10的余数代替
#该数字，再将第一位和第四位交换，第二位和第三位交换。
from sys import stdout
a=int(raw_input('请输入一个四位整数:'))
aa=[]
aa.append(a%10)
aa.append(a%100/10)
aa.append(a%1000/100)
aa.append(a/1000)

for i in range(4):
    aa[i]+=5
    aa[i]%=10
for i in range(2):    
    aa[i],aa[3-i]=aa[3-i],aa[i]
for i in range(3,-1,-1):
    stdout.write(str(aa[i]))   

