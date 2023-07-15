# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:01:28 2023

@author: DELL
"""

#queue using 2 stacks
st1=[]
st2=[]
class node():
  def __init__(self,val):
       self.val=val
       self.next=None
class stackqueue():
    def __init__(self):
        self.head=None
    def enqueue(self,new):
        if self.head==None:
            newnode=node(new)
            self.head=newnode
        else:
            newnode=node(new)
            newnode.next=self.head
            self.head=newnode
    def dequeue(self):
        if self.head==None:
            print("no")
        else:
            c=stackqueue()
            while self.head.next!=None:
                c.enqueue(self.head.val)
            self.head=None
            while c.head!=None:
                self.head.enqueue(c.head.val)
d=stackqueue()
d.enqueue(6)
d.enqueue(7)
d.enqueue(8)
#print(d.head.val)
d.dequeue()
print(d.head.next.val)
            
            
    