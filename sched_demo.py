# coding:utf-8

import time
import sched

# 被调度触发函数


def event_func(msg):
	print("Current Time:", time.time(), 'msg:', msg)

if __name__ == "__main__":
	# 初始化sched模块的scheduler类
	s = sched.scheduler(time.time, time.sleep)
	# 调度

	while True:
		s.enter(1, 2, event_func, ("Small event.", ))
		s.enter(2, 1, event_func, ("Big event.", ))
		s.run()
		time.sleep(10)

