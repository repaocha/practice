#!/usr/bin/python
# -*- coding:utf-8 -*-

#找到年龄最大的人，并输出。

if __name__=='__main__':
    person={"li":18,"wang":50,"zhang":60,"sun":30}
    m='li'
    for i in person.keys():
        if person[m]<person[i]:
            m=i
    print 'the oldest person is：%s,age:%d' % (m,person[m])