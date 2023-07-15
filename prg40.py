# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:07:34 2023

@author: DELL
"""

#poisonous plants using stacks
p=[3,6,2,7,5]
stack=[]
died=0
days=0
while(p):
   died=0
   stack.append(p[0]) 
   for i in range(1,len(p)):
       if p[i-1]>p[i]:
           stack.append(p[i])
       else:
           died=1
   if died==1 :
       days=days+1
   p=stack.copy()
   print(p)
   stack=[]
   if died==0:
      break 
print(days)  
print(p)      