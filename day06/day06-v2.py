# coding:utf-8
import os
import re

'''
    v2 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
'''

# s = [('a', 3), ('b', 2), ('d', 5), ('c', 1)]
#
# print(sorted(s, key=lambda x: x[1]), reversed=True)

# list dir file


def walk_dir(path):
	file_path2 = []
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.lower().endswith('txt'):
				file_path2.append(os.path.join(root, f))
	return file_path2


def find_key_word(filepath):
	word_dict = {}
	filename = os.path.basename(filepath)
	with open(filepath) as f:
		text = f.read()
		word_list = re.findall(r'[A-Za-z]+', text.lower())
		for w in word_list:
			if w in word_dict:
				word_dict[w] += 1
			else:
				word_dict[w] = 1
		sorted_word_list = sorted(word_dict.items(), key=lambda d: d[1])
		print("在%s文件中，%s为关键词，共出现了%s次" % (filename, sorted_word_list[-1][0], sorted_word_list[-1][1]))

if __name__ == "__main__":
	for file_path in walk_dir(os.getcwd()):
		find_key_word(file_path)
