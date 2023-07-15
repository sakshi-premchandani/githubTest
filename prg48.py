# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:19:49 2023

@author: DELL"""

a="101001000"
maxsub=0
res=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        c1=0
        c0=0
        b=a[i:j]
        for k in range(len(b)):
            if b[k]== "1":
                c1=c1+1
            else:
                c0=c0+1
        if c1==c0:
            res=(j-i)+1
            maxsub=max(res,maxsub)
print(maxsub)
                