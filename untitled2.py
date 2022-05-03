# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:41:40 2022

@author: 91703
"""

def printAllKLength(string, k):
	n = len(string)
	printAllKLengthRec(string, "", n, k)

def printAllKLengthRec(string, prefix, n, k):
	if (k == 0) :
		print(prefix)
		return
	for i in range(n):
		newPrefix = prefix + string[i]
		out=printAllKLengthRec(string, newPrefix, n, k - 1)
	
string = input()
string=sorted(string)
k = 3
printAllKLength(string, k)
	
