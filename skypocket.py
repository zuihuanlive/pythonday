#!/usr/bin/python
# coding=utf-8
import os
import datetime
import time
import sched

'''
	mdb_transfer 备份工具,定时备份
'''

mdb_transfer_cmd = '/billcs/bin/mdb_transfer'
mdb_dir = '/billcs/mdb/abm_mdb'
# mdb_dir = '/home/yszc/mdb/abm_mdb'
# Execution Time 24 format
hour = 11
minute = 22

# Accuracy  minute
accuracy = 1


def mdb_transfer(mdb_transfer_cmd, mdb_dir):
	today = datetime.date.today()
	# yesterday = today - datetime.timedelta(days=1)
	yesterday = today.strftime("%Y%m%d")
	flag = 'ABM_CAbmPocket.mdb'

	filenames = os.listdir(mdb_dir)
	files = []
	files_num = 0
	i = 0
	p = 0
	while i < len(filenames):
		if flag in filenames[i]:
			files.append(filenames[i])
			if yesterday in files[p]:
				files_num = p
			p += 1
		i += 1

	if yesterday in files[files_num]:
		cmd_line = mdb_transfer_cmd + " " + files[files_num] + " ud.abmpocket_skyroam_" + yesterday + "  ud/ud@orcl 1 export 1000 data01  oracle"
		os.popen(cmd_line).read()
		# print(cmd_line)
	else:
		exit()

if __name__ == '__main__':
	# 初始化sched模块的scheduler类
	s = sched.scheduler(time.time, time.sleep)

	while True:
		time.sleep(accuracy * 60)
		now_hour = int(time.strftime("%H", time.localtime(time.time())))
		now_minute = int(time.strftime("%M", time.localtime(time.time())))

		if now_hour == hour:
			if now_minute >= minute:
				if now_minute < minute + accuracy:
					# 调度
					s.enter(1, 2, mdb_transfer, (mdb_transfer_cmd, mdb_dir))
					s.run()

