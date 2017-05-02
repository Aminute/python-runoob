#!usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
handle=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handle)
response=opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)