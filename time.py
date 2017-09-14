#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import calendar #年历、日历模块

ticks = time.time()
print("当前时间戳为： " , ticks)

localtime = time.localtime(time.time())
print("本地时间为: ",localtime)

#获取格式化的时间
localtimes = time.asctime(time.localtime(time.time()))
print("格式化时间为： " ,localtimes)

#格式化成2017-09-14 15:28:20
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#格式化成Thu Sep 14 15:28:20 2017
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))

#格式化时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#获取某月日历
cal = calendar.month(2017,9)
print("2017年9月")
print(cal)

print(time.localtime())
