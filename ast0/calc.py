#!/usr/bin/python3 -B

import sys

def calcAst0(l=[]):
	# find tiniest number
	tinyNum=l[0]
	for i in range(1, len(l)):
		if l[i] < tinyNum:
			tinyNum = l[i]
	# bring all numbers to >= 4
	inc = -tinyNum+4
	print("inc=" + str(inc))
	print("before inc: " + str(l))
	for i in range(len(l)):
		oldnum = l.pop(i)
		l.insert(i, oldnum + inc)
	print("before split: " + str(l))
	# find unique nums, split them
	tmp = list()
	for i in range(len(l)):
		if l.count(l[i]) == 1:
			tmp.append(l[i]-2)
			tmp.append(l[i]-2)
		else:
			tmp.append(l[i])
	l = tmp
	print("after split: " + str(l))
	while True:
		l = sorted(l)
		if l[-1] != 2:
			print(l)
			num = l[-1]
			spots = list()
			for i in range(len(l)):
				if l[i] == num:
					spots.append(i)
			for i in sorted(spots, reverse=True):
				l.pop(i)
			for i in range(len(spots)+1):
				l.append(num-1)
		else:
			break
	return len(l) - inc + 2

if __name__ == "__main__":
	print(calcAst0([int(x) for x in sys.argv[1:]]))
