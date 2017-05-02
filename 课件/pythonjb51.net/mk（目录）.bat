@echo off
setlocal EnableDelayedExpansion
del chinaz.com.txt /s
del chinaz.com.txt /s
del 说明.htm /s
del 西西*.* /s
del 东坡*.* /s
del pc6*.* /s
del 使用说明.txt /s
del 东坡软件下载基地.* /s
del 说明.htm /s
del 下载银行.txt /s
del 下载银行-提供免费绿色软件下载.url /s
rem copy d:\jb51tools\jb_down\book\ !cd!
mkdir jb51.net
del %0 | move *.* jb51.net