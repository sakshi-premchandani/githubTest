# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:09:08 2023

@author: DELL
"""

h1=[1,2,3,4]
h2=[6,7,8,9]
maxsum=10
c=[]
isum=0
i=0
while(isum+h1[i]<=maxsum and i<len(h1)):
    isum+=h1[i]
    i=i+1
ans=i
j=0
i=0
while(j<len(h2) and i>=0):
    isum+=h2[j] 
    j=j+1 
    while(isum>maxsum and i>0):
        i=i-1 
        isum-=h1[i]
    if(isum<=maxsum and i+j>ans):
        ans=i+j
print(ans)