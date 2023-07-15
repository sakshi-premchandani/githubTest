# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:57:13 2023

@author: DELL
"""

a=[9,6,3,5,2]
maxs=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        m1=min(a[i:j+1])
        b=a[i:j+1]
        b.remove(m1)
        m2=min(b)
        print(i,j,m2)
        s1=m1^m2
        maxs=max(s1,maxs)
print(maxs)
        
