# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:24:57 2023

@author: DELL
"""

class node():
    def __init__(self,val):
        self.val=val
        self.next=None
class queue():
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,new):
        if self.head==None:
            self.head=node(new)
        else:
            newnode=node(new)
            newnode.next=self.tail
            self.tail=newnode
    def delete(self):
        if self.head==None:
            print("do nothing")
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.next
    def view(self,index):
        pointer=self.head
        while(index):
            pointer=pointer.next
        print(pointer.val)
    def length(self):
        count=0
        point=self.head
        while(point.next!=None):
            point=point.next
            count=count+1
        print(count)
c=queue()
c.insert(5)
c.insert(4)
c.insert(6)
print(c.head.val)
print(c.tail.val)
c.delete()
#print(c.head.val)
