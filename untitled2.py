# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:18:52 2023

@author: DELL
"""
maxsum=15
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
c=stack()
c.insert(1)
c.insert(2)
c.insert(3)
c.insert(4)
d=stack()
d.insert(5)
d.insert(6)
d.insert(7)
d.insert(8)
