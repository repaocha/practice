#!/usr/bin/python
# -*- coding:utf-8 -*-

#�Ӽ�������һЩ�ַ������������д�������ļ��ϣ�ֱ������һ�� # Ϊֹ��

if __name__ == '__main__':
    from sys import stdout
    filename = raw_input('�����ļ���:\n')
    fp = open(filename,"w")
    ch = raw_input('�����ַ���:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = raw_input('')
    fp.close()