from ast import Delete
from xml.dom.minidom import TypeInfo


## Python does not have built-in support for Arrays, but Python Lists can be used instead.

arr = [1,2,3,4, "hello"]
arr2 = [1,2,3,4,6]
print(arr)
print(type(arr)) #list
print(type(arr2)) #list

arr2.insert(0, 5)
print(arr2) #could be time consuming depending upon the index it's inserting at as it shifts the list accordingly, output: 5,1,2,3,4

#other methods, append - to add at the end, and extend() to append a list to another list. simple a + b is equivalent to extend() for lists a & b

#[5, 1, 2, 3, 4, 6]
arr2.pop(2) #index based, default is the last element. Time consuming as it shifts the elements accordingly.
print("pop method: ", arr2) #output = pop method:  [5, 1, 3, 4, 6]


arr2.remove(5) #value based, not index based. Useful when you know the value/item to be removed but don't know the index of the same. 
                            #or same value from multiple places to be removed in a list 
print(arr2) #output: 1,2,3,4

#delete method
del arr2[1]
del arr2[1:4] #possible too
print(arr2)