# coding:utf-8
import os

"""
统计ftp指定目录下文件数量
"""

dir1 = '/JFJSJ/Download/files'
# dir2 = '/JFJSJ/Download/files'

ftp_user = 'username'
ftp_pass = 'passwd'
ftp_host = '127.0.0.1'

result = 0

cmd = 'echo \"cd '+dir1+';ls\"|lftp '+ftp_user+':'+ftp_pass+'@'+ftp_host+'|wc -l'

result = int(os.popen(cmd).read())

print(result)
