#!/usr/bin/python
# -*- coding: UTF-8 -*-

n=int(raw_input('请输入n:\n'))
a=int(raw_input('请输入a:\n'))

i=0
su=0
bei=1
for i in (0,n):
    su+=a*bei;
    bei=bei*10+1
print'最后的总和为%d'%su
