#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��ϰ�������á�

def hello_world():
    print 'hello world'

def three_hello():
    for i in range(3):
        hello_world()
        
if __name__=='__main__':
    three_hello()