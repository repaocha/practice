#!/usr/bin/python
# -*- coding:UTF-8 -*-

#求输入数字的平方，如果平方运算后小于50则退出。

import math
a=int(raw_input('请输入数字:'))
s=a*a
if s<50:
    print '程序停止运行'
else:
    print s