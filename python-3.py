#!/usr/bin/env python
# coding=utf-8

#字符串格式化
form = 'Hello %s,%s enough for ya'
value = ('world','Hot')
print form % value

form = 'Pi with three decimals %.3f'
from math import pi
print form % pi

from string import Template
s = Template('$x,glorious $x!')
print s.substitute(x = 'slurm')

s = Template("Is's ${x}tastic")
print s.substitute(x = 'slurm')

s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d)

#通过元组格式化
print '%s plus %s equals %s' % (1, 1, 2)

#字符格式化(完整版)
print 'Price of eggs:$%d' % 42
print 'Using str:%s' % 42L
print 'Using repr:%r' % 42L
print '%10f' % pi
print '%10.2f' % pi
print '%.2f' % pi
#可以用＊作为字段宽度或精度
print '%.5s' % 'Guido van Rossum'
print '%.*s' % (5,'Guido van Rossum')
#符号(+)，对其(-)，0填充(0)，空白("")
print '%+10.2f' % -pi
print '%+10.2f' % pi
print '%-10.2f' % pi
print '%010.2f' % pi
print '% 10.2f' % pi
print '% 10.2f' % -pi

#字符串方法
temp = 'With a moo-moo here, and a moo-moo there'
print temp.find('moo')
print 'moo' in temp
#设定起始点
print temp.find('moo',8)
#设定结束点
print temp.find('moo',0,23)
print temp.find('moo',13,33)


#join
seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq)
dirs = ['', 'usr', 'bin', 'env']
print '/'.join(dirs)
print 'C:' + '\\'.join(dirs)

#lower
print 'ABCD'.lower()
#title
print "that's all folks".title()
#capwords
import string
print string.capwords("that's all folks")
#replace
print 'this is a test'.replace('test', 'shit')
#split
print '1+2+3+4+5'.split('+')
#如果不提供分隔符，程序会吧所有空格作为分隔符
print '1 2345'.split()
#strip
string = '     internal whitespace is kept     '.strip()
print string
string = '***spam * for * everyone !!!***'.strip('*')
print string
#translate(第一个参数是转换表，第二个参数是要删除的字符)
#转换表
from string import maketrans
table = maketrans('cs', 'kz')
print len(table)
print 'this is a incredible test'.translate(table)
print 'this is a incredible test'.translate(table,' ')
#translate与replace的不同在于
#replace可以替换字符串中的某一部分
#translate可以只处理单个字符