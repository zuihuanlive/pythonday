#!/usr/bin/env python
#coding: utf-8

import os,re,sys,time,paramiko,multiprocessing

#读取账户文件中的信息进行存储
def get_userinfo():
    #读取数据
    f = open('user_info','r')
    cont = f.readlines()
    f.close()
    uinfo = []

    #print cont
    #分割处理
    for i in cont:
        p = re.compile(r'\s+')
        t = p.split(i)
        #存储账户信息到字典
        d = {}
        d['ip'] = t[0]
        d['user'] = t[1]
        d['passwd'] = t[2]
        d['port'] = t[3]
        uinfo.append(d)
    return uinfo

userinfo = get_userinfo()


result = []

#远程执行命令函数
def command(ip,user,passwd,port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #连接服务器
    ssh.connect(ip,int(port),user,passwd)
    #执行命令
    stdin, stdout, stderr = ssh.exec_command("hostname;df -h;free -m;who")
    #打印输出正确结果
    print  ip,stdout.read()
    #say(ip,stdout.read())
    #打印输出错误结果
    #print stderr.read()


#p = multiprocessing.Pool(processes=len(userinfo)-1)
p = multiprocessing.Pool(8)

for i in userinfo:
    result.append(p.apply_async(command,('%s'%i['ip'],'%s'%i['user'],'%s'%i['passwd'],'%s'%i['port'])))

p.close()

for res in result:
    res.get(timeout=30)
