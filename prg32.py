# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:33:29 2023

@author: DELL
"""

class node():
    def __init__(self,val):
        self.val=val
        self.next=None
class queue():
    def __init__(self):
        self.head=None
    def insert(self,new):
        if self.head==None:
            newnode=node(new)
            self.head=newnode
        else:
            newnode=node(new)
            point=self.head
            while(point.next!=None):
                point=point.next
            point.next=newnode
    def pop(self):
        if self.head==None:
            print("do nothing")
        elif self.head.next==None:
            print(self.head.val)
            self.head=None
        else:
            print(self.head.val)
             self.head=self.head.next
    def length(self):
        if self.head==None:
            print("empty")
        else:
            point=self.head
            while(point.next!=None):
                point=point.next
                count=count+1
    def view(self):
        if self.head==None:
            print("nothing to print")
        
           
c=queue()
c.insert(5)
c.insert(4)
print(c.head.val)
print(c.head.next.val)