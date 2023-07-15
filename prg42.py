# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:49:02 2023

@author: DELL
"""

stack=[]
string=""
for _ in range(int(input())):
    t=input().split()
    if t[0]=='1':
        stack.append(string)
        string+=t[1]
    elif t[0]=='2':
        stack.append(string)
        string=string[:-int(t[1])]
    elif t[0]=='3':
        print(string[t[1]-1])
    else:
        string=stack.pop()