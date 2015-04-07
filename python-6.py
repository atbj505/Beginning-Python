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
    for i in range(num - 2):
        fib.append(fib[i] + fib[i+1])
    return fib
print fibonacci(6)

#纪录函数 __doc__
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
change(names)
print names

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
print lookup(testName, 'middle', '')

#关键字参数
def hello(greeting, name):
    print '%s, %s' % (greeting, name)

hello('Hello', 'World')
hello(greeting = 'Hello', name = 'World')

#默认值
def hello_1(greeting = 'Hello', name = 'World'):
    print '%s, %s' % (greeting, name)
hello_1
hello_1(name = 'Robert')

#收集函数 *参数为长度任意元组 **参数为长度任意字典
def print_params_1(*params):
    print params

print_params_1('1', '2', '3')

def print_params_2(title,*params):
    print title,params
print_params_2('title','1','2','3')
print_params_2('nothing')

def print_params_3(**params):
    print params
print_params_3(x=1, y=2, z=3)

def print_params_4(x, y, z = 3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar
print_params_4(1, 2, 3, 4, 5, 6, foo=1, bar=2)

def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data = data, label = label, name = name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]
testName = {}
init(testName)
store(testName, 'Luke Skywalker', 'Anakin Skywalker')
print lookup(data = testName, label = 'last', name = 'Skywalker')

#反转
def add(x, y):
    return x + y
#将元祖当作参数传入
params = (1, 2)
print add(*params)
#将字典当作参数传入
dic = {'x':1, 'y':2}
print add(**dic)

def with_stars(**kwds):
    print kwds['name'], 'is', kwds['age'], 'years old.'
def without_stars(kwds):
    print kwds['name'], 'is', kwds['age'], 'years old.'
ages = {'name':'Mr.Gumby', 'age':42}
with_stars(**ages)
without_stars(ages)

def foo(x, y, z, m=0, n=0):
    print x, y, z, m, n
def call_foo(*args, **kwds):
    print 'Calling foo'
    foo(*args, **kwds)
args = (1, 2, 3)
dic = {'m':4, 'n':5}
call_foo(*args, **dic)

#练习
def story(**kwds):
    return 'Once upon a time, there was a '\
            '%(job)s called %(name)s.' % kwds
def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)
def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop == None:
        start, stop=0, start
#这条语句等价与 stop = start, start = 0
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

#指定参数
print story(job='king', name='Gumby')
print story(name='Sir Robin', job='brave knight')
#字典分割参数
params = {'job':'language', 'name':'python'}
print story(**params)
del params['job']
print story(job='stroke of genius', **params)

print power(2, 3)
print power(3, 2)
print power(x=2, y=3)
params = (2,)*2
print power(*params)
print power(3, 3, 'Hello World')

print interval(10)
print interval(0, 10)
print interval(0, 10, 2)

print power(*interval(3,8))

#作用域 每个函数都会创建一个新的作用域
x = 1
#vars可以返回作用域的键值字典
scope = vars()
print scope['x']
scope['x'] += 1
print x

def foo():
    x = 42
    print x
foo()
print x

def output(x):
    print x
x = 1
y = 2
output(y)

def combine(parameter):
    print parameter + external
external = 'berry'
combine('straw')

#globals() global
def combine(parameter):
    print parameter + globals()['parameter']
parameter = 'berry'
combine('straw')

x = 1
def change_global():
    global x
    x = x + 1
change_global()
print x

#闭包
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
double = multiplier(2)
print double(5)
print multiplier(4)(5)

#递归
def factorial(n):
    if n == 1:
        return n;
    else:
        return n * factorial(n-1)
print factorial(4)

def pow(n,m):
    if m == 1:
        return n
    else:
        return n * pow(n, m-1)
print pow(2, 3)

def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if sequence[middle] > number:
            return search(sequence, number, lower, middle)
        else:
            return search(sequence, number, middle+1, upper)
sequence = [4, 32, 7, 89, 103]
sequence.sort()
print sequence
params = (sequence, 103)
print search(*params)

#map 可以讲序列中的元素传递给一个函数
print map(str, range(10))
print [str(i) for i in range(10)]

#filter 可以通过一个返回值为布尔行的函数对数据进行过滤
def func(x):
    return x.isalnum()
seq = ['foo', 'X41', '?!', '***']
print filter(func, seq)
seq = ['foo', 'X41', '?!', '***']
print [x for x in seq if x.isalnum()]

#lambda 匿名函数
print filter(lambda x: x.isalnum(), seq)

#reduce
numbers = [72, 101, 32]
print reduce(lambda x,y:x+y,numbers)
