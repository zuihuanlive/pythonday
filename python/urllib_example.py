#!/usr/bin/env python
#coding: utf-8

import urllib

url = 'http://www.baidu.com'
data = urllib.urlopen(url).read()
data = data.decode('UTF-8')
print (data)