#!/usr/bin/python
# -*- coding:UTF-8 -*-

#�������飬�������һ��Ԫ�ؽ�������С�������һ��Ԫ�ؽ�����������顣

a=[1,4,5,7,8,9,2,0,3]
print a

min=min(a)
a.remove(min)   #�Ƴ�
a.append(min)   #�ӵ������

max=max(a)
a.remove(max)    #�Ƴ�
a.insert(0,max)  #���뵽��һ��

print a
