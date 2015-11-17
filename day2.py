# coding:utf-8

import os

for root, dirs, files in os.walk('/home/zuilive/PycharmProjects'):
    for f in files:
        print(f)

