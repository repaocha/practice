#!/usr/bin/python
# -*- coding:UTF-8 -*-

#����һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ�����
s = raw_input('������һ���ַ�:')
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
print 'Ӣ����ĸ: %s,�ո�: %s,����:%s,����:%s' % (letters,space,digit,others)