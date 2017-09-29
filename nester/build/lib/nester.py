#’’’’’’’’’’’’’’’’’’’’’Something need to know, study''''''''''''''''''''''''''''''
#coding=utf-8
#isinstance(isList, list) 判断isList是否是列表
#range(n) 返回一个[0，1，2，…，N-1] 的迭代器
#’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
import sys

'''indent, level are default parameter'''
def print_lol(the_list, indent = False, level = 0, fh = sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level + 1, fh)
		else:
			if indent:
				for tab_num in range(level):
					print("\t", end='', file = fh)
			print(each_item, file = fh)








''' example:
movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
		['Graham Chapman',
			['Michael Palin', 'Johh Cleese', 'Terry Gillam', 'Eric Idle', 'Terry Jones']]]

print_lol(movies)
'''
