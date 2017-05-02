#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(100,1000):
    i=num/100
    j=(num%100)/10
    k=(num%100)%10
    if (i*i*i+j*j*j+k*k*k==num):
        print'%d'%num
