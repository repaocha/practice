#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��һ���������ֽ���������

def prime(n):
    l = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                l.append(i)
                break    
    return l


s = input("����һ��������:")
if  int(s) > 0:
    print(s, '=', "*".join([str(x) for x in prime(int(s))]))
else:
    print("��������ȷ��������")