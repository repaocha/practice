#!/usr/bin/python
# -*- coding:UTF-8 -*-

#���������������Ƕ������ɴ��⣺ѧϰ�ɼ�>=90�ֵ�ͬѧ��A��ʾ��60-89��֮�����B��ʾ��
#60�����µ���C��ʾ��
score = int(raw_input('�������:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
 
print '%d ���� %s' % (score,grade)