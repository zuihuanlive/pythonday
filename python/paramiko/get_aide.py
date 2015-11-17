#!/usr/bin/env python
#coding: utf-8
import re
import paramiko
import time
import os

#读取账户文件中的信息进行存储
def get_userinfo():
    #读取数据
    f = open('user_info','r')
    cont = f.readlines()
    f.close()
    uinfo = []
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

#下载文件
def get_file(ip,user,passwd,port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    trans = paramiko.Transport((ip,int(port)))
    trans.connect(username=user,password=str(passwd))
    sftp = paramiko.SFTPClient.from_transport(trans)
    today = str(time.strftime("%Y%m%d"))
    remotepath = '/usr/local/aide/aide-'+today+'.log'
    localdir = '/home/zuilive/systeminfo/'+ip
    localpath  = localdir+'/aide-'+today+'.log'
    #print remotepath,localpath
    #判断本地目录是否存在
    if not os.path.isdir(localdir):
        #建立目录
        os.mkdir(localdir)
    #下载
    sftp.get(remotepath,localpath)

userinfo = get_userinfo()
for i in userinfo:
    get_file(i['ip'],i['user'],i['passwd'],i['port'])
