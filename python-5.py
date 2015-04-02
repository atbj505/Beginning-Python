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
x , y ,z = value
print x

scoundrel = {'name':'Robin', 'girlfriend':'Marion'}
key, value = scoundrel.popitem()
print key
print value

#增量赋值
fnord = 'foo'
fnord += 'bar'
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