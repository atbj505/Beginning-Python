#!/usr/bin/env python
# coding=utf-8

#抽象
fib = [0, 1]
for i in range(8):
    fib.append(fib[i] + fib[i+1])
print fib

#callable 判断函数是否可用
import math
x = 1
y = math.sqrt
print callable(x)
print callable(y)

#def 函数的定义
def hello(name):
    return 'Hello,' + name
print hello('robert')

def fibonacci(num):
    fib = [0 ,1]
    for i in (num - 2):
        fib.append(fib[i] + fib[i+1])
print fib
fibonacci

#纪录函数
def square(x):
    'Calculates the square of the number x.'
    return x*x
print square.__doc__

#help
help(square)

#return
def test():
    print 'This is printed'
    return
    print 'This is not'
x = test()
print x

#参数
def try_to_change(n):
    n = 'Mr.Gumby'
name = 'Mrs.Entity'
try_to_change(name)
print name

def change(n):
    n[0] = 'Mr.Gumby'
names = ['Mrs.Entity', 'Mrs.Thing']

#n 是行参的复制
change(names[:])
print names
#n 是行参的引用 本质是指针
change(names)
print names

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1,'')
    labels = ['first', 'middle', 'last']
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]#以列表保存

testName = {}
init(testName)
print testName
store(testName, 'Robert Yang')
store(testName, 'Robert Wang')
print testName
print lookup(testName, 'first', 'Robert')
