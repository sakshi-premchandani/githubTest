# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:49:04 2023

@author: DELL
"""

#find nth prime no
count=0
n=4
num=1
while(count<=n):
    num=num+1
    i=2
    for i in range(num+1):
        if num%i==0:
            break
    if num==i:
        count=count+1
print(num)
    