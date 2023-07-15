# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 20:12:33 2023

@author: DELL
"""
count=0
for i in range(1,1001):
    if(i%3==0 and i%7==0):
        count=count+1
print(count)
#using o(1) methoud
firstterm=21
lastterm=1000
d=21
print((lastterm-firstterm)//d+1)    