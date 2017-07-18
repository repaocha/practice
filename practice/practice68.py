#!/usr/bin/python
# -*  coding:UTF-8 -*-

#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数。

from collections import deque
m=int(raw_input('向后移m个位置:'))
n=int(raw_input('n个整数:'))
a=[]

for i in range(n):
   a.append(int(raw_input('输入一个数字:')))
print '开始时列表：', a
   
f=deque(a)     #双端队列
f.rotate(m)   #旋转队列，默认向右旋转，m为负值时向左旋转
print '移动后列表：', list(f)