#!/usr/bin/python
# -*-coding:UTF-8 -*-

#������������x,y,z,�������������С���������

x=int(raw_input('����integer:'))
y=int(raw_input('����integer:'))
z=int(raw_input('����integer:'))

l=[x,y,z]
l.sort()
print '����������С�����˳��:',l
n=[x,y,z]
n.sort(reverse=True)
print '���������ɴ�С��˳��:',n