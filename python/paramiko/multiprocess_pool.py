#coding:utf-8
import multiprocessing
import sys,os,time

result = []

def run(ip,user):
    print 'threading test:',ip,user,os.getpid()
    time.sleep(2)

p = multiprocessing.Pool(processes=25)
di = [{'ip':12,'user':'abc'},{'ip':13,'user':'bbc'}]
for i in di:
    result.append(p.apply_async(run,('%s'%i['ip'],'%s'%i['user'])))

p.close()

for res in result:
    res.get(timeout=5)
