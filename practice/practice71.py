#!/usr/bin/python
# -*- coding:UTF-8 -*-

#��дinput()��output()�������룬���5��ѧ�������ݼ�¼��

N=5
student=[]
for i in range(5):
    student.append(['','',[]])
    
def input_stu(stu):
    for i in range(N):
        stu[i][0]=raw_input('input student num:')
        stu[i][1]=raw_input('input student name:')
        for j in range(3):
            stu[i][2].append(int(raw_input('score:')))
def output_stu(stu):
    for i in range(N):
        print '%-6s%-10s' % (stu[i][0],stu[i][1])
        for j in range(3):
            print '%-4d' % stu[i][2][j]

if __name__=='__main__':
    input_stu(student)
    print student
    output_stu(student)