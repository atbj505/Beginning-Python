#!/usr/bin/env python
# coding=utf-8
#列表
edward = ['Edward Gumby',42]
john = ['John Smith',50]
dataBase = [edward,john]
print dataBase


#索引
greeting = 'Hello'
print greeting[0]
print greeting[-1]

#分片
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]
print numbers[0:1]
print numbers[-4:-2]
print numbers[-1:0]
print numbers[7:]
print numbers[:]
#步长
print numbers[::2]
print numbers[::-1]

#列表相加
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print numbers1 + numbers2
#列表相乘
print numbers1 * 4
#空列表
sequence = [None] * 10
print sequence
#成员资格
permissions = 'rw'
print 'w' in permissions
dataBase = [['albert', '1234'],
            ['dilbert', '4242'],
            ['smith', '7524'],
            ['jones', '9843']]
print ['albert', '1234'] in dataBase
print 'albert' in dataBase


#长度 最大值 最小值
numbers = [100, 34, 678]
print len(numbers)
print max(numbers)
print min(numbers)

#List 对象->列表的转换
print list('Hello')

#元素赋值
x = [1, 2, 3]
x[0] = 0
print x
#删除元素
del x[2]
print x
#分块赋值(可以赋值为与元列表不等长的列表)
x[0:] = ['x', 'x', 'x']
print x
#插入新的元素
numbers = [1, 10]
numbers[1:1] = [2, 3, 4, 5, 6, 7, 8, 9]
print numbers
#改变步长插入
numbers[0:10:2] = ['x'] * 5
print numbers
#删除元素
numbers[1:4] = []
print numbers
#append
lst = ['1', '2', '3']
lst.append(4)
print lst
#count
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1)
print x.count([1, 2])
#extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print a
#a.extend(b) 与 a + b的区别在于
#a.extend(b)是在b的基础上把a的元素添加进去
#a + b是返回一个新的列表
a = [1, 2, 3]
b = [4, 5, 6]
print a + b
print a
#也可以通过分片实现相同的结果
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print a
#index
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a.index(4)
#insert
a = [1, 2, 3, 5]
a.insert(3,4)
print a
#pop 移除最后一个元素(默认)并返回该元素的值(列表中唯一有返回值的方法)
x = [1, 2, 3]
print x.pop()
print x.pop(0)
print x
#模拟栈:append类似于压栈操作，pop是出栈操作
x = [1, 2, 3]
x.append(x.pop())
print x
#模拟队列操作:pop(0)
x = [1, 2, 3]
x.append(4)
x.pop(0)
print x
#remove:移除第一个匹配项
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print x
#reverse
x = [1, 2, 3]
x.reverse()
print x
#reversed
x = [1, 2, 3]
print reversed(x)
print list(reversed(x))
#reverse方法返回一个列表
#reversed函数返回一个迭代器对象

#sort
x = [4, 6, 2, 1, 7, 9]
x.sort()
print x
x = [4, 6, 2, 1, 7, 9]
#注意不能使用y = x
#这样是使y和x指向同一列表
#要想复制列表需要用到y = [:]
y = x[:]
x.sort()
print x
print y

#sorted
#sorted与.sort的区别在于
#sorted不会修改元列表而会返回排序结果给一个新的列表
#.sort是直接修改元列表的排序
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print sorted(x)
print x
print y
#高级排序
print cmp(42, 32)
print cmp(99, 100)
print cmp(10, 10)
numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers
#指定key排序,reverse反制
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key = len, reverse = True)
print x



#元组 不可修改的序列
print (1, 2, 3)
print (42,)
print 3 * (40 + 2)
print 3 * (40 + 2,)
print 3 * (40, + 2)
#tuple 序列->元祖的转换
print [1, 2, 3]
print tuple([1, 2, 3])
print tuple('tuple')
print tuple((1,2,3))
#元组基本操作
x = 1, 2, 3
print x
print x[1]
print x[:2]

#元组与列表的区别
#1.元组可以在映射中当作键使用
#2.元组作为内建函数的方法返回值存在

#小结
#序列是一种数据结构
#典型的序列包括列表，字符串，元组
#列表可变，字符串和元组是不可变的
#list()->序列转化成列表
#tuple()->序列转化成元组
