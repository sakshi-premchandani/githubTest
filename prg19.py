# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:50:19 2023

@author: DELL
"""

#manipulation of array
query=[[1,5,3],[4,8,7],[6,9,1]]
n=10
b=[]
for i in range(n):
    b.append(0)
for j in range(len(query)):
    for z in range(query[j][0]-1,query[j][1]):
        b[z]=b[z]+query[j][2]
    print(b)
print(max(b))