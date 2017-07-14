#!/usr/bin/python
# -*- coding:UTF-8 -*-

#求100之内的素数。

for num in range(2,101):
    for i in range(2,num):
     if (num%i)==0:
         break
    else:
        print(num)
    