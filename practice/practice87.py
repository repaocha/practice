#!/usr/bin/python
# -*- coding:utf-8 -*-

#回答结果（结构体变量传递）

class student:
    x=0
    y=0
def f(stu):
    stu.x=20
    stu.y='c'
a=student()
a.x=2
a.y='b'
f(a)
print a.x,a.y