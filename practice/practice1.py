#!/usr/bin/python
# -*- coding: UTF-8 -*-

#有四个数字：1,2,3,4，能组成多少个互不相同且不重数字的三位数？各是多少？

d=[]               
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (x!=z) and(y!=z):
                d.append([x,y,z])
                print x,y,z
print "总数量:", len(d)
print d