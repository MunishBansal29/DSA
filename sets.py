#A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. 

# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for 
# checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. 
# Since sets are unordered, we cannot access items using indexes as we do in lists.

myset = {1,2,3,4,5,6,6,7,7}
print(myset) #output : {1, 2, 3, 4, 5, 6, 7} i.e. removes duplicates

#convert a list into set
mylist = [11,80,13,14,15,16,16,11,12,80]
myset = set(mylist)
print(myset) #{11, 12, 13, 14, 15, 80, 16} -> order is not guranteed

#traversing sets
#can not be traversed using indexes or keys, i.e. full set can be printed, compared or used


#adding elements
myset.add(100)
print(myset) #{100, 11, 12, 13, 14, 15, 80, 16}

#union
set1 = {1,2,3,4,5,5}
set2 = {7,7,6,8,9,10}
set3 = set1 | set2
print(set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(sorted(set3)) #returns a list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#intersection i.e. common
set1 = {1,2,3,6,7,9,10}
set2 = {3,2,6,8,11}
print(set1 & set2) #{2, 3, 6}

#difference
set1 = {1,2,3,6,7,9,10}
set2 = {3,2,6,8,11}
print(set1 - set2) #{1, 10, 9, 7} -> what set1 has which set2 does not have
print(set2 - set1) #{8, 11} -> what set2 has which set1 does not have

#comparision
set1 = {1,3,5,7}
set2 = {1,2,3,4,5,6,7}
if set1 < set2:
    print("set2 is superset of set1") #works
# IN operator does not work in above











