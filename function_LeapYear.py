# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:16:02 2022

@author: Mahendra Nath Reddy E
"""


def is_leap(year):
    if(year%4==0 and year%100 !=0 or year%400==0):
        return True
    else:
        return False

    
    
year=int(input())
print(is_leap(year))