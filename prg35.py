# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:15:27 2023

@author: DELL
"""

A=[2,3,4,5,6,7]
q=3
ans=[]
def prime(n):
    count=0
    num=1
    while(count<n):
       num=num+1
       for i in range(2,num+1): 
           if i!=0 and num%i==0:
            break 
       if num==i:
         count=count+1 
    return num
b=[]
for k in range(1,q+1):
    num=prime(k)
    temp=[]
    j=len(A)-1
    while j>=0:
        if A[j]%num!=0:
            temp.append(A.pop())
        else:
            b.append(A.pop())
        j=j-1
    ans=b.copy()
    A=temp.copy()
print(ans)

    
    
    
    
            
    
    