#!/usr/bin/python
# -*- coding:UTF-8 -*-

#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

a=[1,4,5,7,8,9,2,0,3]
print a

min=min(a)
a.remove(min)   #移除
a.append(min)   #加到最后面

max=max(a)
a.remove(max)    #移除
a.insert(0,max)  #插入到第一个

print a
