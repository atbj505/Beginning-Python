#!/usr/bin/env python
# coding=utf-8
#字典 python中唯一的映射

phoneBook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3258'}
print phoneBook
print phoneBook['Beth']
#dict
items = [('name', 'Gumby'),('age', '42')]
d = dict(items)
print d
print d['name']
d = dict(name = 'Gumby', age = 42)
print d

print len(d)
d['age'] = 25
print d
del d['age']
print d
print 'age' in d
#字典的格式化字符串
print phoneBook
print "Cecil 's phone number is %(Cecil)s" % phoneBook

#clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
d.clear()
print d

#{}与clear()的区别
#x = {}只会使x指向一个空字典
#x.clear()会清空x指向的内存
x = {}
y = x
x['key'] = 'value'
print x
print y
x = {}
print x
print y

x = {}
y = x
x['key'] = 'value'
print x
print y
x.clear()
print x
print y

#copy
x = {'username':'admin', 'machines':['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
print x
print y
y['machines'].remove('baz')
print x
print y

#deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print d
print c
print dc

#赋值(=) 浅拷贝(copy) 深拷贝(deepcopy)
import copy
a = [1, 2, 3, 4, ['a', 'b']]

b = a #赋值 对象的引用
c = copy.copy(a) #对象拷贝，浅拷贝
d = copy.deepcopy(a) #对象拷贝，深拷贝

a.append(5)
print a
print b
print c
print d

a[4].append('c')
print a
print b
print c
print d

#fromkeys
a = {}.fromkeys(['name', 'age'])
print a
print dict.fromkeys(['name', 'age'])
print dict.fromkeys(('name', 'age'))
print dict.fromkeys(['name', 'age'],'unknown')

#get
d = {}
print d.get('name')
print d.get('name','N/A')
d['name'] = 'Eric'
print d.get('name')
print d['name']

#has_key
d = {}
print d.has_key('name')
d['name'] = 'Eric'
print d.has_key('name')

#items
d = {'title':'python web site', 'url':'http://www.python.org', 'spam':0}
print d.items()

#iteritems
it = d.iteritems()
print it
print list(it)

#keys
print d.keys()

#iterkeys
it = d.iterkeys()
print it
print list(it)

#pop
d = {'x':1, 'y':2}
d.pop('x')
print d

#popitem
d = {'title':'python web site', 'url':'http://www.python.org', 'spam':0}
d.popitem()
print d

#setdefault
d = {}
d.setdefault('name', 'N/A')
print d
d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print d
d = {}
print d.setdefault('name')

#update
d = {
    'title':'python web site',
    'url':'http://www.python.org',
    'changed':'Mar 14 22:09:15 MET 2008'
}
x = {'title':'python language website'}
d.update(x)
print d
