#!/usr/bin/python
# -*- coding:utf-8 -*-

#字符串日期转换成易读的日期格式。

from dateutil import parser
dt=parser.parse("Jul 19 2017 18:00PM")
print dt