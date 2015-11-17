#coding:utf-8

from multiprocessing import Process,Lock

import time,os

def sayhi(i):
    print 'hello world',i
    time.sleep(10)

for n in range(100):
    p = Process(target=sayhi,args=(n,))
    p.start()
