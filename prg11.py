# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 20:35:47 2023

@author: DELL
"""

a=[1,3,5,6,5,7,6,9]
b=[]
b.append(a[0])
for i in range(1,len(a)-1):
        if(a[i+1]<a[i]):
            b.append(a[i+1])
        elif(a[i+1]==a[i]):
            continue
        else:
            b.append(a[i])
print(b)
    
    