# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:14:35 2023

@author: DELL
"""

a=[5,6,3,7,2,9,4,8]
for i in range(len(a)):
    for i1 in range(i+1,len(a)):
        if a[i]<a[i1]:
            c=a[i]
            a[i]=a[i1]
            a[i1]=c
print(a)        