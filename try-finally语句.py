#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("����һ�������ļ������ڲ����쳣!!")
finally:
    print "Error: û���ҵ��ļ����ȡ�ļ�ʧ��"