# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:49:01 2023

@author: DELL
"""

h=[3,2,1,3,3,4]
mul=1
maxi=0
for i in range(len(h)):
    c=1
    for j in range(i+1,len(h)):
        if(h[i]<=h[j]):
            c=c+1
        else:
            break
    mul=h[i]*c 
    maxi=max(maxi,mul)
print(maxi)