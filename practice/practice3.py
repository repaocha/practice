#!/usr/bin/python
# -*- coding:UTF-8 -*-

#һ��������������100����һ����ȫƽ�������ټ���168����һ����ȫƽ������
#���ʸ����Ƕ��٣�

for i in range(1,85):
    if 168 % i ==0:
        j=168/i
        if i>j and (i+j)%2==0 and (i-j)%2==0:
            m=(i+j)/2
            n=(i-j)/2
            x=n*n-100
print x
             