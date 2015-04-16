#/usr/bin/env python
#coding=utf-8

#异常
#raise Exception('hyperdrive overlaod')

#系统异常
import exceptions
print dir(exceptions)

#raise ArithmeticError

#自定义异常类
class SomeCustomException(Exception):pass

#捕捉异常
try:
    x = 10;
    y = 0;
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero"
except TypeError:
    print "That wasn't a number,was it"

#屏蔽异常
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator = MuffledCalculator()
print calculator.calc('10/2')
calculator.muffled = True
print calculator.calc('10/0')

#一个块捕捉两个异常
try:
    x = 10
    y = 3
    print x/y
except(ZeroDivisionError, TypeError, NameError):
    print 'Your numbers were bogus...'

#捕捉对象
try:
    x = 10
    y = 0
    print x/y
except(ZeroDivisionError, TypeError), e:
    print e

#全捕捉
try:
    x = 10
    y = 0
    print x/y
except:
    print 'Something wrong happened'

#else
try:
    print 'A simple task'
except:
    print 'What? Something went wrong?'
else:
    print 'Ah...It went as planned.'

while True:
    try:
        x = 10
        y = 2
        value = x/y
        print 'x/y is', value
    except Exception,e:
        print 'Invalid input:',e
        print 'Please try again'
    else:
        break

#finally
try:
    1/1
except NameError:
    print 'Unknow variable'
else:
    print 'That went well!'
finally:
    print 'Cleaning up'

#函数中的异常
def faulty():
    raise Exception('Something is wrong')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'
#ignore_exception()
handle_exception()

def describePerson(person):
    print 'Descriptin of',person['name']
    print 'Age:',person['age']
    try:
        print 'Occupation:' + person['occupation']
    except KeyError:
        pass
person1 = {'name':'Robert', 'age':'25', 'occupation': 'IT'}
person2 = {'name':'Lucy', 'age':'23'}
describePerson(person1)
describePerson(person2)
