#!/usr/bin/python
# -*- coding:utf-8 -*-

#ʱ�亯�� 

if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))