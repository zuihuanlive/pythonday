#!/usr/bin/env python
#coding: utf-8

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect("10.10.30.29",22,"jboss", "asiainfo312")
#执行命令
stdin, stdout, stderr = ssh.exec_command("df -h")
#打印输出正确结果
print stdout.readlines()
#打印输出错误结果
print stderr.readlines()


#下载文件
trans = paramiko.Transport(('10.10.30.29'),22)
trans.connect(username='jboss',password='asiainfo312')
sftp = paramiko.SFTPClient.from_transport(trans)

remotepath = '/apps/jboss/bb1.py'
localpath  = '/home/zuilive/zuilive.py'

#下载文件
sftp.get(remotepath,localpath)

#上传文件
sftp.put(localpath,remotepath)

#关闭连接
ssh.close()