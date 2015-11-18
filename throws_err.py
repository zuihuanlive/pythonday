# coding:utf-8

'''
	python 中的异常
'''

# NameError 尝试访问一个没有声明的变量
try:
	foo
except NameError as e:
	print('尝试访问一个没有声明的变量:', e)

# ZeroDivisionError 除数为零
try:
	2/0
except ZeroDivisionError as e:
	print('除数为零:', e)

# SyntaxError: Python解释器语法错误

# IndexError 请求索引超出序列范围
try:
	alist = []
	alist[0]
except IndexError as e:
	print('请求索引超出序列范围', e)


# KeyError 请求一个不存在的字典关键字
try:
	adict = {'host': 'earth', 'port': 80}
	print(adict['zuilive'])
except KeyError as e:
	print('请求一个不存在的字典关键字:', e)

# IOError: 输入输出错误
try:
	f = open('zuilive')
except IOError as e:
	print('输入输出错误:', e)


# AttributeError: 尝试访问未知的对象属性


class myClass(object):
	pass
try:
	myInst = myClass()
	myInst.bar = 'zuilive'
	print(myInst.foo)
except AttributeError as e:
	print('尝试访问未知的对象属性:', e)


# 处理多个异常可以使用多个except,或者是将多个异常放入一个元组
obj = []
try:
	retval = float(obj)
except (ValueError, TypeError):
	retval = 'argument must be a number or numeric string'

print(retval)
