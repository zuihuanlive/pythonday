#!/usr/bin/python
#coding: utf-8

####################################
#   银盛项目升级补丁脚本 v1
#   zuihuanxiang@126.com
#   实现：新增文件、替换文件、删除文件
#   2015/09/11
####################################
import os
import sys
import time


#执行shell命令， 参数：路径  命令
def executeCmd(cmd_line):
	return os.popen(cmd_line).read()
	
#检查文件或目录是否存在
def checkFile(file_path):
	if os.path.exists(file_path):
		pass
	else:
		print ('文件或目录：'+file_path+'不存在！')
		exit()
		
#备份应用函数
def backupApp(deploy_path,backup_path):
	#建立备份目录
	if os.path.exists(backup_path):
		print ('备份目录：'+backup_path+' 已存在')
		exit()
	else:
		os.mkdir(backup_path)
		for i in deploy_path:
			cmd_line = 'cp -rf '+i['path']+' '+backup_path
			#print cmd_line
			os.popen(cmd_line).read()
			print (i['path']+' 备份完成！')

#生成替换后文件的MD5信息并存储
def md5Check(patch_dir,patch_list,md5_file):
	patch_md5 = open(md5_file,'w+')
	for i in patch_list:
		cmd_line = 'md5sum '+os.path.join(i['path'],i['file'])
		#print cmd_line
		cmd_result = (executeCmd(cmd_line)).split(' ')
		#print cmd_result
		patch_md5.write(cmd_result[0]+'  '+i['file']+'\n')
		
	patch_md5.close()


	
#获取当前路径
pwd_path = os.getcwd()
patch_dir = os.path.join(pwd_path,'patch_file')
checkFile(patch_dir)
md5_file = os.path.join(patch_dir,'patch.md5')

patch_file = open(pwd_path+'/patch_file.txt','r')
path = patch_file.readlines()
patch_file.close()

#初始化
stop_app = []
deploy_path = []
patch_list = []
delete_list = []

for eachline in path:
	#去除回车
	eachline = eachline.strip('\n')

	#去除空行
	if eachline[:-1].split():
		file_list = eachline.split('\t')   #按照tab进行分割
	#print (file_list[0])
		if file_list[0].upper() == 'S':
			#print ('停止应用')	
			checkFile(file_list[1])
			stop_app.append(file_list[1])
		
		elif file_list[0].upper() == 'DEPLOY_PATH':
			#print ('部署路径')
			checkFile(file_list[1])
			flag = {'path':file_list[1]}
			d_path = file_list[1]
			deploy_path.append(flag)
		
		elif file_list[0].upper() == 'B':
			#print ('备份路径')
			checkFile(file_list[1])
			flag = {'path':file_list[1]}
			#当前时间
			today = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
			backup_path =  os.path.join(flag['path'],today)

		elif file_list[0].upper() == 'A' or file_list[0].upper() == 'R':
			#print ('替换或新增文件')
			flag = {'type':file_list[0].upper(),'path':os.path.join(d_path,file_list[1]),'file':file_list[2]}
			if file_list['0'].upper() == 'R':
				checkFile(os.path.join(d_path,file_list[1],file_list[2]))
			checkFile(os.path.join(patch_dir,file_list[2]))
			patch_list.append(flag)
		
		elif file_list[0].upper() == 'D':
			#print ('删除文件')
			checkFile(os.path.join(d_path,file_list[1],file_list[2]))
			flag = {'type':file_list[0].upper(),'path':os.path.join(d_path,file_list[1]),'file':file_list[2]}
			delete_list.append(flag)
		
		else:
			print (file_list[0]+' 操作符错误！请检查下patch_file.txt文件！')
			exit()

#备份应用
print ('开始备份应用......')
backupApp(deploy_path,backup_path)

#停止应用
for i in stop_app:
	executeCmd(i)
	print ('已停止'+i)


############打补丁
#替换文件，新增文件
for i in patch_list:
	#print i
	cmd_line = 'cp '+os.path.join(patch_dir,i['file'])+' '+os.path.join(i['path'],i['file'])
	executeCmd(cmd_line)
	if i['type'] == 'A':
		print (i['file']+' 已新增')
	else:
		print (i['file']+' 已替换')


#删除文件
for i in delete_list:
	cmd_line = 'rm '+os.path.join(i['path'],i['file'])
	executeCmd(cmd_line)
	print (i['file']+' 已删除')
	


print ('============MD5校验=============')
md5Check(patch_dir,patch_list,md5_file)
cmd_line = 'md5sum -c '+md5_file
os.chdir(patch_dir)
print (executeCmd(cmd_line))


