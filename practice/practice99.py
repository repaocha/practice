#!/usr/bin/python
# -*- coding: UTF-8 -*-

#�����������ļ�A��B,�����һ����ĸ,Ҫ����������ļ��е���Ϣ�ϲ�(����ĸ˳������), �����һ�����ļ�C�С�

if __name__ == '__main__':
    import string
    fp = open('yangchen.txt')
    a = fp.read()
    fp.close()

    fp = open('test.txt')
    b = fp.read()
    fp.close()

    fp = open('test1.txt','w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()