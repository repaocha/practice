#!/usr/bin/python
# -*- coding: UTF-8 -*-

#��n����Χ��һȦ��˳���źš��ӵ�һ���˿�ʼ��������1��3��������������3�����˳�Ȧ�ӣ���������µ���ԭ���ڼ��ŵ���λ��

n=int(input("��������:"))
List=[]
for i in range(1,n+1):
    List.append(i)

sum=0
while 1:
    t=0;
    for i in range(1,len(List)+1):
        sum=sum+1
        if (sum)%3==0:
            List.pop(i-1-t)
            t=t+1

    if len(List)==1:
        print("������µ���ԭ����%d�ŵ���λ" % List[0])
        break