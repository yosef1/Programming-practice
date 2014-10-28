#!/usr/bin/python
# open a list of words, sort them, and output them sorted

list = [line.strip() for line in open('test-data/wordlist.txt')]

option = raw_input('Output list in ascending(1) or descending(0) order? ')
if option == "1" or option == "asc":
	newlist = sorted(list, key=str.lower)
elif option == "0" or option == "desc":
	newlist = sorted(list, key=str.lower, reverse=True)


file = open('output/newwordlist.txt', 'w+')
for item in newlist:
	print>>file, item
file.close()