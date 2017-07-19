#!/usr/bin/python
# -*- coding:UTF-8 -*-

#列表排序及连接,连接可以使用a+b或者extend()方法。

a=[1,3,2,4]
b=[5,7,6,8]
a.sort()
b.sort()
print a
print b
print a+b

a.extend(b)
print a
