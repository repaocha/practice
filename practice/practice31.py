#!/usr/bin/python
# -*- coding:UTF-8 -*-

#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
letter=raw_input('请输入字母:')
if letter=='M':
    print ('Monday')

elif letter=='T':
    raw_input('请输入第二个字母:')
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
    raw_input('请输入第二个字母:')
    if letter=='a':
        print 'Saturday'
    elif letter=='u':
        print 'Sunday'
    else:
        print 'Wrong Data'
else:
    print ('Wrong Data')