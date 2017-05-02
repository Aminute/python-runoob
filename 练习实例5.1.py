#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = int (raw_input('num1:\n'))
y = int (raw_input('num2:\n'))
z = int (raw_input('num3:\n'))

if (x>y):
    d=x
    x=y
    y=d
if (y>z):
    d=y
    y=z
    z=d
if (x>y):
    d=x
    x=y
    y=d
print'%d'%x
print'%d'%y
print'%d'%z
