#!/usr/bin/env python
# coding=utf-8

#条件，循环和其他
print 'age', 42

#print
name = 'Gumby'
salution = 'Mr'
greeting = 'Hello'
print greeting, salution, name
print greeting + ',', salution, name
print 'Hello,',
print 'world'

#赋值语句
x, y, z = 1, 2, 3
print x, y, z
x, y = y, x
print x, y, z

value = 1, 2, 3
print value
x , y , z = value
print x, y, z

scoundrel = {'name':'Robin', 'girlfriend':'Marion'}
key, value = scoundrel.popitem()
print key
print value

#增量赋值
fnord = 'foo'
fnord += 'bar '
fnord *= 2
print fnord

#条件和条件语句
print bool('I think, therefore I am')
print bool(42)
print bool('')
print bool(0)

#if-else
name = 'I am Gumby'
if name.endswith('Gumby'):
    print 'Hello Mr.Gumby'
else:
    print 'Hello stanger'

if name.endswith('Gumby'):
    if name.startswith('Mr'):
        print 'Hello Mr.Gumby'
    else:
        print 'Hello Miss.Gumby'
else:
    print 'Hello stanger'

#elif
number = 1
if number > 0:
    print 'The number is positive'
elif number < 0:
    print 'The number is negative'
else:
    print 'The number is zero'

#is 判断统一性(是不是同一对象)
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z # false

x = [1, 2, 3]
y = [2, 4]
print x is not y
del x[2]
y[1] = 1
y.reverse()
print x == y
print x is y

#in
name = "Robert"
if 'o' in name:
    print "name contains the letter 'o'"
else:
    print "name not contains the letter 'o'"

#字符串比较
print 'alpha' < 'beta'
print 'a' < 'b'
print 'l' < 'e'
print 'al' < 'be'

print 'FnOrD'.lower() == 'Fnord'.lower()
print [1, 2] < [2, 1]
print [1, 2] < [2]
print [1, 2] < 2

# and(&) or(|) not
n = 8
if n >= 0 & n <= 10:
    print 'Greate'
else:
    print 'Wrong'

m = 0
if n | m:
    print 'Right'
else:
    print 'Wrong'

if not m:
    print 'Right'
else:
    print 'Wrong'

#三元运算符
print 'a' if 'b' else 'c'
print 'a' if 0   else 'c'
a = 10;
b = 0;
print 'Right' if a > b else 'wrong'

#断言
age = 10
assert 0 < age < 100
age = -1
#assert 0 < age < 100 'The age must be realistic'

#循环
x = 1
while x <= 100:
    print x
    x += 1

words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word

print range(0, 10)
for number in range(100):
    print number

d = {'x': 1, 'y':2, 'z':3}
print d.items()
for lis in d.items():
    print lis
for key, value in d.items():
    print key,value

#并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = ['12', '45', '32', '102']
#for(int i = 0; i < names.count; i++)
for i in range(len(names)):
    print names[i] + ' : ' + ages[i]
#zip
print zip(names, ages)
for name, age in zip(names, ages):
    print name + ' : ' + age

for index, string in enumerate(names):
    if 'anne' in string:
        names[index] = 'robert'
print names
#sorted reversed
print sorted([4, 3, 6, 8, 3])
print reversed("Hello world")
print list(reversed('Hello world'))
print ''.join(reversed('Hello world'))

#跳出循环
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print root, n
        break

while True:
    i += 1
    if i == 5:
        print 'i = %d' % i
        break

#循环中的else
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it"

#列表推倒式
print [x*x for x in range(10)]
print [x*x for x in range(10) if x%3 == 0]
print [(x, y) for x in range(3) for y in range(3)]

girls = ['alice', 'bernice', 'clarice']
boys = ['chris' 'arnold', 'bob']
print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]

#pass 空白分支占位
name = 'Enid'
if name == 'Ralph Auldus Melish':
    print 'Welcome'
elif name == 'Enid':
    pass
elif name == 'Bill Gates':
    print 'Access denied'

#del
x = ['Hello', 'World']
y = x
y[1] = 'Python'
print x
print y
del x
print y
x = []
print x
print y

#exec
exec "print 'Hello world'"

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print len(scope)
print scope.keys()

#eval
print eval('1 + 1')
scope = {}
scope['x'] = 2
scope['y'] = 3
print eval('x * y',scope)
exec 'x = 4' in scope
print eval('x * x', scope)
