#!/usr/bin/env python3
#coding: utf-8
import platform
print (platform.python_version())

def story(**kwds):
	return 'Once upon a time, there was a %s called %s.' %(kwds['job'],kwds['name'])


#print story(job='king',name='Gumby')

def interval(start, stop=None,step=1):
	'Imitaties range() for step > 0'
	if stop is None:
		start,stop = 0,start

	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result

print (interval(10))
print (interval(1,30,3))

#修改全局变量
x = 1
def change_global():
	global x
	x = x+1
change_global()
print (x)
change_global()




