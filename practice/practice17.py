#!/usr/bin/python
# -*- coding:UTF-8 -*-

#输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。
s = raw_input('请输入一行字符:')
letters = 0
space = 0
digit = 0
others = 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print '英文字母: %s,空格: %s,数字:%s,其他:%s' % (letters,space,digit,others)