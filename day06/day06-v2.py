# coding:utf-8
import os
import re

'''
    你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
'''


def get_file(path):
    # 列出文件
    file_list = os.listdir(path)
    print(file_list)
    return file_list


def get_topword(file_name):
    # open file
    f = open(file_name, 'r')
    word_list = re.split(r'\W+', f.read())
    # to lower
    flag = 0
    for i in word_list:
        word_list[flag] = i.lower()
        flag += 1
    word_list.sort()

    flag = 0
    record = {}
    for i in word_list:
        top_num = word_list.count(i)
        if top_num > flag:
            flag = top_num
    # print(flag)

    for i in word_list:
        top_num = word_list.count(i)
        if top_num == flag and i not in record:
            record[i] = flag
    return record

file_list = get_file(os.getcwd())
for i in file_list:
    print(get_topword(i), 'file:%s' % i)

