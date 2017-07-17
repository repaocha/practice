#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 数字比较

x=raw_input('请输入x:')
y=raw_input('请输入y:')

if x>y:
    print '%s大于%s' % (x,y)
elif x==y:
    print '%s等于%s' % (x,y)
elif x<y:
    print '%s小于%s' % (x,y)
else:
    print '未知'