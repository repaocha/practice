#!/usr/bin/python
# -*- coding:UTF-8 -*-

#һ�������ǡ����������֮�ͣ�������ͳ�Ϊ��������������6=1+2+3.����ҳ�1000���ڵ�����������
for i in range(1, 1001):
    sum = 0
    k=[]
    for j in range(1, i):
        if i % j == 0:
            sum += j
            k.append(j)    
    if sum == i:
        print(i)
