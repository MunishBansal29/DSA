#single linked list

from ctypes import addressof
from hashlib import new
from pty import slave_open

from jinja2 import TemplateNotFound

class slnode:
    def __init__(self, val=None):
        self.Value = val
        self.Next = None

class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def iterList(self):
        lsNode = self.head    
        while lsNode is not None:
            print(lsNode.Value)
            lsNode = lsNode.Next

    def insertlinklist(self, value, location):
        #create a new node
        newNode = slnode(value)
        if self.head is None: #i.e. no node exists into the linkedlist
            self.head = newNode
            self.tail = newNode
        else:    
            if location == 0: #point new node's next to head, and then head to newnode
                newNode.Next = self.head
                self.head = newNode
            elif location == -1: #i.e. to be inserted at the end
                newNode.Next = None
                self.tail.Next = newNode
                self.tail = newNode
            else:           #adding anywhere else in the linkedlist per given location (should be valid)
                #need to traverse through till the given location    
                index = 0
                tempNode = self.head
                while index < location - 1: #if given location is more than total number of node available, it should insert it at the end
                    if tempNode.Next is None:
                        break
                    tempNode = tempNode.Next
                    index += 1
                nextNode = tempNode.Next    
                tempNode.Next = newNode
                newNode.Next = nextNode            

sl = singleLinkedList()
node1 = slnode(10)
node2 = slnode(20)

sl.head = node1
node1.Next = node2
sl.tail = node2

print(node1.Value, '->', node1.Next.Value) # 10->20

print(id(sl.head), id(node1)) #4491165120 4491165120 => both points to the same location.
print(id(sl.tail), id(node2)) #4369315728 4369315728 => both points to the same location.

#this requires to traverse the linked list and find the last element in the list i.e. where address is equal to tail
sl.iterList() # 10 20

sl.insertlinklist(30, 2)
sl.iterList() # 10 20 30

sl.insertlinklist(5, 0) #insert at the begining
sl.iterList() # 5, 10 20 30










