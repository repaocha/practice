#!/usr/bin/python
# -*- coding:utf-8 -*-

#ĳ����˾���ù��õ绰�������ݣ���������λ���������ڴ��ݵĹ������Ǽ��ܵģ����ܹ������£�ÿ�����ֶ�����5��Ȼ���úͳ���10����������
#�����֣��ٽ���һλ�͵���λ�������ڶ�λ�͵���λ������
from sys import stdout
a=int(raw_input('������һ����λ����:'))
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

