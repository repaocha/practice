#!/usr/bin/python
# -*- coding:utf-8 -*-

#�ַ�������

if __name__=='__main__':
    list1=[]
    str1=raw_input('�������ַ���:\n')
    str2=raw_input('�������ַ���:\n')
    str3=raw_input('�������ַ���:\n')
    print str1,str2,str3
    
    list1=[str1,str2,str3]
    list1.sort()
    print list1
    
    #list1.extend([str1,str2,str3])
    #list2=sorted(list1)
    #print list2