# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 21:31:24 2023

@author: DELL
"""

#reverse the array
a=[1,2,3,4]
for i in range(round(len(a)/2)):
    #swap(a[i],a[len(a)-i])
    c=a[i]
    a[i]=a[len(a)-i-1]
    a[len(a)-i-1]=c
print(a)
        
        
       