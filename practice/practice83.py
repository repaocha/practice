#!/usr/bin/python
# -*- coding:utf-8 -*-

#��0��7������ɵ�����������

sum=4
s=4
for i in range(2,9):
    if i<=2:
        s*=7
    else:
        s*=8
    sum+=s
print 'sum=%d' % sum