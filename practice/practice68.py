#!/usr/bin/python
# -*  coding:UTF-8 -*-

#��n��������ʹ��ǰ�����˳�������m��λ�ã����m���������ǰ���m������

from collections import deque
m=int(raw_input('�����m��λ��:'))
n=int(raw_input('n������:'))
a=[]

for i in range(n):
   a.append(int(raw_input('����һ������:')))
print '��ʼʱ�б�', a
   
f=deque(a)     #˫�˶���
f.rotate(m)   #��ת���У�Ĭ��������ת��mΪ��ֵʱ������ת
print '�ƶ����б�', list(f)