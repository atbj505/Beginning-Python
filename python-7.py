#/user/bin/env python
#coding=utf-8

#类和对象

#系统类型多态
from random import choice
x = choice(['Hello, world', [1, 2, 'e', 'e', 4]])
print x
print x.count('e')

def lenth_message(x):
    print 'The lenth of %s is %s' % (repr(x), len(x))
lenth_message('Fnord')
lenth_message([1, 2, 3])

#类
#新式类
__metaclass__ = type
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world! I'm %s" % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()

print foo.name
bar.name = 'Robert'
bar.greet()

#方法＝函数
class Class:
    def method(self):
        print 'I have a self!'
def function():
    print "I don't"
instance = Class()
instance.method()
instance.method = function
instance.method()

#变量＝方法
class Bird:
    song = 'Squaawk!'
    def sing(self):
        print self.song
bird = Bird()
bird.sing()
birdSong = bird.sing
birdSong()

#私有化
class Secretive:
    def __inaccessible(self):
        print "Bet you can't see me..."
    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
s = Secretive()
s.accessible()
#私有方法名变为_类名方法名
s._Secretive__inaccessible()

#类命名空间
class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
print m1.members
print MemberCounter.members
m2 = MemberCounter()
m2.init()
print m2.members
print MemberCounter.members
m1.members = 'Two'
print m1.members
print m2.members
print MemberCounter.members

#超类
class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']
f = Filter()
f.init()
print f.filter([1, 2, 3])
s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'eggs', 'bacon'])

#检查继承
#判断继承关系
print issubclass(SPAMFilter, Filter)
print issubclass(Filter, SPAMFilter)
#查看父类
print SPAMFilter.__bases__
print Filter.__bases__
#判断实例化关系
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
print isinstance(s, str)
#查看实例类型
print s.__class__

#多继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print 'Hi,my value is %s' % self.value
class TalkingCaculator(Calculator, Talker):
    pass
tc = TalkingCaculator()
tc.calculate('1+2+3')
tc.talk()
#注意超类继承的顺序
#如果两个超类中有同名方法则写在前面的超类方法会覆盖写在后面的超类方法

#接口和内省
print hasattr(tc, 'talk')
print hasattr(tc, 'fbord')

print callable(getattr(tc, 'talk', None))
print callable(getattr(tc, 'fnord', None))

setattr(tc, 'name', 'Mr.Gumby')
print tc.name
