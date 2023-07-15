# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:00:12 2023

@author: DELL
"""
def eq(x):
    y=x**3-4*x-9
    return y
for i in range(-10,10):
    if eq(i)<0:
       a=i
       break 
for j in range(-100,100):
    if eq(j)>0:
       b=j
       break 
#range is (a,b)
#print(a,b)
while(1):
    mid=(a+b)/2
    vmid=eq(mid)
    if abs(vmid)<0.00001:
        print(vmid,mid)
        break
    else:
        if(vmid>0.00001):
             b=mid
        elif(vmid<0.00001):
             a=mid
    #print(mid,a,b)