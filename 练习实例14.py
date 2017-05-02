#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fenjie(n):
    print'{}='.format(n),
    if not isinstance(n,int)or n<=0:
        print'请输入一个正确的数字'
        exit(0)
    while n not in[1]:
        for i in range(2,n+1):
            if(n%i==0):
                if(n==i):
                    print'{} '.format(i)
                else:
                    print'{}*'.format(i),
                n=n/i
                break

fenjie(9.3)
fenjie(100)
