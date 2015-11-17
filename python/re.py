#!/usr/bin/python
#coding: utf-8

import re


#~ p = re.compile(r'hello')
#~ m = p.match('hello world')
#~ #print (m.group())
#~ #print('你好')
#~ 
#~ t = re.match(r'hello','hello world')
#~ print (t.group())

#~ p = re.compile(r'\d+')
#~ 
#~ t = p.split('1one2two3three4four',1)
#~ print (t) 


p = re.compile(r'\d')
t = p.findall('1one211two311three42four')
print (t)

print (re.sub('[abc]','o','mark'))
