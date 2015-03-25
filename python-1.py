#!/usr/bin/env python
# coding=utf-8

#整除相关头文件
from __future__ import division
#0.5
print 1 / 2
#0
print 1 // 2
#0.0
print 1.0 // 1.2
#3
print 10 // 3
#1
print 10 % 3
#8
print 2 ** 3
#-9
print -3 ** 2
#9
print (-3) ** 2


#幂 8
print pow(2,3)
#绝对值 10
print abs(-10)
#四舍五入 1
print round(1.0 / 2.0)


#算数模块
import math
#向上取整
print math.floor(32.9)
#向上取整
print math.ceil(32.9)


#通过模块引入函数
from math import sqrt
#平方跟
print sqrt(9)


import cmath
#虚数
print cmath.sqrt(-1)

#Hello World!
x = 'Hello '
y = 'World!'
print x + y
#'Hello World!'
print repr('Hello World!')
#Hello World!
print str('Hello World!')


#3
#input('Enter a number')
#'3'
#raw_input('Enter a number')


#原始字符串
print r'/n/n/n'
#Unicode
print u'/n/n/n'