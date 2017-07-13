#!/usr/bin/python
#　-*-coding:UTF-8 -*-

#一球从100米高度自由落下，每次落地后反跳回原高度的一半，求它在第10次落地时，共经过多少米？
#第10次反弹多高？
   
tour=[]
height=[]

h=100.0
time=10
for i in range(1,time+1):
    if i==1:
        tour.append(h)
    else:
        tour.append(2*h)
    hei /= 2
    height.append(h)
print('总长度：tour={0}'.format(sum(tour)))
print('第10次反弹高度：%s' % (min(height)))