# coding:utf-8
import re

'''
    任一个英文的纯文本文件，统计其中的单词出现的个数
'''


def count(filepath):
    f = open(filepath, 'rb')
    s = f.read()
    # words = re.findall(r'[a-zA-Z0-9]+', s)
    words = re.findall(r'\w+')
    return len(words)

if __name__ == '__main__':
    num = count('word.txt')
    print num
