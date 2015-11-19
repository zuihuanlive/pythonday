# coding:utf-8

# import os
import datetime
import  time

# for root, dirs, files in os.walk('/home/zuilive/PycharmProjects'):
#     for f in files:
#         print(f)

exec_time = '02:30'
exec_time.split(':')
hour = exec_time[0]
minute = exec_time[1]
# today = datetime.date.today()
# now = datetime.date.ctime()
# now = time.ctime
today = int(time.strftime("%M", time.localtime(time.time())))
print(today+1)

