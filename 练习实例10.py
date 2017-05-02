#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#暂停1秒
time.sleep(2)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
