#!/usr/bin/python
# coding=utf-8
import os
import datetime

#####################
#   zuilive
#   2015-8-12
#
#   下载服务器日志
#####################

today = datetime.date.today()
yesterday = today-datetime.timedelta(days=1)
yesterday = yesterday.strftime("%Y%m%d")


file_name = 'ua_aaaService' + yesterday+'.log'
log_path = '/apps/radius/ua/bin/log'
local_path = '/apps/172_16_148_18/radius'
err_file = 'ua_aaaService_err'+ yesterday + '.log'

# 压缩日志
cmd_line = 'ssh radius@172.16.148.18 \'cd '+log_path+' ;tar -czvf '+file_name+'.tar.gz '+file_name+'\''
os.popen(cmd_line).read()

# 下载日志
cmd_line = 'scp radius@172.16.148.18:'+log_path+'/'+file_name+'.tar.gz '+local_path
os.popen(cmd_line).read()

# 删除压缩的日志
cmd_line = 'ssh radius@172.16.148.18 \'rm '+log_path+'/'+file_name+'.tar.gz\''
os.popen(cmd_line).read()

# 下载error日志
cmd_line = 'scp radius@172.16.148.18:'+log_path+'/'+err_file+' '+log_path
os.popen(cmd_line)
