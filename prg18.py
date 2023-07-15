# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:18:01 2023

@author: DELL
"""
#squareroot
#y^2-x=0
def eq(y):
    z=y**2-9
    return z
for i in range(-100,100):
    if eq(i)<0:
        a=i
        break
for j in range(-100,100):
    if eq(j)>0:
        b=j
        break
while(1):
    mid=(a+b)/2
    vmid=eq(mid) 
    if(abs(vmid)<0.00001):
        print(mid)
        break
    else:
        if vmid>0:
            b=mid
        elif vmid<0:
            a=mid 