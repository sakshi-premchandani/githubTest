# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:23:13 2023

@author: DELL
"""
#poisonous plants
p=[3,6,2,7,5]
temp=[]
while(p):
    for i in range(1,len(p)):
        if(p[i]>p[i-1]):
            temp.append(i)   #[1.3]
    print(temp)
    if(len(temp)!=0):
        for j in range(len(temp)):
           p.pop(temp[j])
            if j<len(temp)-1:
                temp[j+1]=temp[j+1]-1
    else:
         break
 print(p)