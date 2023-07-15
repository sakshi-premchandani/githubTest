# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:45:19 2023

@author: DELL
"""
#left rotate
arr=[1,2,3,4,5]
#shift 1 time
n=2
while(n):
    for i in range(len(arr)-1):
         c=arr[i]
         arr[i]=arr[i+1]
         arr[i+1]=c
    n=n-1
print(arr)