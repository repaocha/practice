#!/usr/bin/python
# -*- coding:UTF-8 -*-
from django.db.models.lookups import Day

#输入某年某月某日，判断这一天是这一年的第几天？

year=int(raw_input('year:'))
month=int(raw_input('month:'))
day=int(raw_input('day:'))

months1=(0,31,59,90,120,151,181,212,243,273,304,334)
months2=(0,31,60,91,121,152,182,213,244,274,305,335)

if ((year%4==0) and (year%100!=0)) or ((year%100==0) and (year%400==0)):
     data=months2[month-1]+day
else:
    data=months1[month-1]+day
print "是该年的第%s天" % data        
