#!/usr/bin/python
# -*- coding:UTF-8 -*-

#���������ڼ��ĵ�һ����ĸ���ж�һ�������ڼ��������һ����ĸһ����������жϵڶ�����ĸ��
letter=raw_input('��������ĸ:')
if letter=='M':
    print ('Monday')

elif letter=='T':
    raw_input('������ڶ�����ĸ:')
    if letter=='u':
        print 'Tuesday'
    elif letter=='h':
        print 'Thursday'
    else:
        print 'Wrong Data'

elif letter=='W':
    print 'Wednesday'

elif letter=='F':
    print 'Friday'
    
elif letter=='S':
    raw_input('������ڶ�����ĸ:')
    if letter=='a':
        print 'Saturday'
    elif letter=='u':
        print 'Sunday'
    else:
        print 'Wrong Data'
else:
    print ('Wrong Data')