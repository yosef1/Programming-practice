#!/usr/bin/python
# open a list of words, sort them, and output them sorted

list = [line.strip() for line in open('wordlist.txt')]
newlist = sorted(list, key=str.lower)

file = open('newwordlist.txt', 'w+')
for item in newlist:
	print>>file, item
file.close()