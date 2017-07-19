#!/usr/bin/python
# -*- coding: UTF-8 -*-

#有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

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