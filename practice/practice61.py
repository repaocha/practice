#!/usr/bin/python
# -*- coding:UTF-8 -*-

#´òÓ¡³öÑî»ÔÈı½Ç

n =10
def yang(i,j):
    if i==j or j==1:
        return 1
    else:
        return yang(i-1,j-1) + yang(i-1,j)
for i in range(1,11):
    for j in range(1,i+1):
        print yang(i,j),
    print