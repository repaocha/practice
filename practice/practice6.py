#!/usr/bin/python
# -*- coding:UTF-8 -*-

#ì³²¨ÄÇÆõÊýÁÐ
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print fib(10)

def fib1(n):
    if n==1 or n==2:
       return 1
    return fib1(n-1)+fib1(n-2)
print fib1(10) 