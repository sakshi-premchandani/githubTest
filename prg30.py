# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:12:46 2023

@author: DELL
"""

s="{(([])[])[]]}"
class node():
  def __init__(self,val):
       self.val=val
       self.next=None
class stack():
    def __init__(self):
        self.head=None
    
    def insert(self,new):
        if self.head == None:
            self.head=node(new)
        else:
            newnode=node(new)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head == None:
           print("no") 
        else:
            self.head=self.head.next
main_st=stack()
if(len(s)%2==0):
    for i in range(len(s)):
        if s[i]=='{'or s[i]=='('or s[i]=='[':
            main_st.append(s[i])
        elif s[i]=='}' and main_st[-1]=='{' or s[i]==']' and main_st[-1]=='[' or s[i]==')' and main_st[-1]=='(':
            main_st.pop()
    if(len(main_st)==0):
        print("yes")
    else:
        print("no")
else:
    print("no")