# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:15:12 2023

@author: DELL
"""
b=[]
a="raipur"
for i in range(len(a)): 
    print(a[0:i+1])
i=len(a)
while(i>0):
    print(a[0:i])
    i=i-1
for i in range(len(a)):
    print(a[i:0])