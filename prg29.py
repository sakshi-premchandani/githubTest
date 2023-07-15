# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:03:09 2023

@author: DELL
"""

operations=['1 97','1 72','3','1 34','3','2']
main_stack=[]
max_stack=[0]
res=[]
for var in operations:
    var=var.split()
    if var[0]=='1':
        main_stack.append(int(var[1]))
        max_stack.append(max(int(var[1]),max_stack[-1]))
    elif var[0]=='2':
        main_stack.pop()
        max_stack.pop()
    else:
        res.append(max_stack[-1])
print(res)        
    