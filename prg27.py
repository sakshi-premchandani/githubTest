# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:17:21 2023

@author: DELL
"""

#prefix sum method
a=[]
queries=[[1,5,3],[4,8,7],[6,9,1]]
a=[0]*10
for i in queries:
    a[i[0]-1]+=i[2]
    if i[1]!=len(a):
         a[i[1]]-=i[2]  
for i in range(1,len(a)): 
    a[i]=a[i-1]+a[i] 
print(max(a))
    