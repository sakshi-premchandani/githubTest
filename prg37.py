# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:04:09 2023

@author: DELL
"""

#largest rectangle
a=[2,3,3,4,5,2,1]
maxarea=0
for i in range(len(a)):
    left=i
    right=i
    while(left>=0 and a[i]<=a[left]):
        left=left-1
    while(right<=len(a)-1 and a[i]<=a[right]):
        right=right+1
    b=right-left-1
    area=a[i]*b
    maxarea=max(maxarea,area)
print(maxarea)
    
     