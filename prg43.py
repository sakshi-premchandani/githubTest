# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 21:37:17 2023

@author: DELL
"""

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
ans=[]
q=4
number=[3,4,7,6,5]
for k in range(1,q+1):
     num=prime(k)
     temp=[]
     j=len(number)-1
     while j>=0:
         if number[j]%num!=0:
             temp.append(number.pop())
         else:
            b.append(number.pop())
         j=j-1
     while b:
         ans.append(b.pop())
     number=temp.copy()
print(ans)