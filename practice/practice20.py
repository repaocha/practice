#!/usr/bin/python
#��-*-coding:UTF-8 -*-

#һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룬�����ڵ�10�����ʱ�������������ף�
#��10�η�����ߣ�
   
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
print('�ܳ��ȣ�tour={0}'.format(sum(tour)))
print('��10�η����߶ȣ�%s' % (min(height)))