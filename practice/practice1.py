#!/usr/bin/python
# -*- coding: UTF-8 -*-

#���ĸ����֣�1,2,3,4������ɶ��ٸ�������ͬ�Ҳ������ֵ���λ�������Ƕ��٣�

d=[]               
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (x!=z) and(y!=z):
                d.append([x,y,z])
                print x,y,z
print "������:", len(d)
print d