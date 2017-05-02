#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout

count=0
tmp=0
for i in range(101,200):
    num1=int(sqrt(i))
    tmp=0
    for j in range(2,num1+1):
        if (i%j==0):
            tmp=1
            break 
    if (tmp==0):
        count=count+1
        print '%d'%i
    if (count==10):
        print''

print'the total is %d'%count
