#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��s=a+aa+aaa+aaaa+......,����a��һ�����֣�����������ɼ��̿���
Sn=[]
m=0
n=int(raw_input('n:'))
a=int(raw_input('a:'))

for count in range(n):
    m=m+a
    a=a*10
    Sn.append(m)
    print m
    
Sn=reduce(lambda x,y:x+y,Sn)
print "�����Ϊ:",Sn
        