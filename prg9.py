# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 21:07:16 2023

@author: DELL
"""

a=[[1,2,3],[4,5,6],[7,8,9]]
print(len(a))
print(len(a[0]))
b=[]
for i in range(len(a)):
    b=b+a[i]
print(b)