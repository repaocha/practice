#!/usr/bin/python
# -*- coding:utf-8 -*-

#�б�ʹ��ʵ��

testList=[10086,'China Mobile',[1,2,4,5]]  
  
#�����б���  
print len(testList)  
#���б��β  
print testList[1:]  
#���б����Ԫ��  
testList.append('i\'m new here!')  
  
print len(testList)  
print testList[-1]  
#�����б�����һ��Ԫ��  
print testList.pop(1)  
print len(testList)  
print testList  

matrix = [[1, 2, 3],  
[4, 5, 6],  
[7, 8, 9]]  
print matrix  
print matrix[1]  
col2 = [row[1] for row in matrix]#get a  column from a matrix  
print col2  
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item  
print col2even  