#!/usr/bin/python
# open a list of words, sort them, and output them sorted

list = [line.strip() for line in open('test-data/wordlist.txt')]
newlist = sorted(list, key=str.lower, reverse=True)

file = open('output/newwordlist.txt', 'w+')
for item in newlist:
	print>>file, item
file.close()