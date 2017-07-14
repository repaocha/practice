#!/usr/bin/python
# -*- coding:UTF-8 -*-

#按相反的顺序输出列表的值。
####按逗号分隔列表。

l=('1','2','3','4','5')
dig='-'
print dig.join(l)

L=(1,2,3,4,5)
s='*'.join(str(n) for n in L)
print s