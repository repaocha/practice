#!/usr/bin/python
# -*- coding:utf-8 -*-

#809*？？+1是四位数，其中？？代表的是两位数，8*？？的结果为2位数，9*？？的结果为3位数。求？？代表的两位数
#及809*？？后的结果。

x=809
for i in range(10,100):
    y=x*i+1
    if y>=1000 and y<10000 and 8*i<100 and 9*i>=100:
        print y