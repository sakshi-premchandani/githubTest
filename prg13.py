# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:42:14 2023

@author: DELL
"""

a=[20,30,40,50,60,70,80,90]
left=0
right=len(a)-1
while(1):
    mid=int((left+right)/2)
    if(a[mid]>60):
        right=mid
    elif(a[mid]<60):
        left=mid
    else:
        break
    print(left,right,mid)
print(mid)