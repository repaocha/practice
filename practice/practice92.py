#!/usr/bin/python
# -*- coding:utf-8 -*-

#ʱ�亯��

if __name__=='__main__':
    import time
    start=time.time()
    for i in range(3000):
        print i
    
    end=time.time()
    print end-start