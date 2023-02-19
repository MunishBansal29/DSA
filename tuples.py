#tuple is immutable sequence of objects

#immutable - 
#...and hence hashable as they don't change over time.

tup = (1,2,3)
print(tup)

#, to be added for one element tuple
tup = (2,) #if comma if not added, it will be treated as normal value like 2 else if a tuple it would be as (2)
print(tup)

#create empyt tuple
tup = tuple()
print(tup) # ()
#OR
tup = ()

tup = tuple('1234')
print(tup) # ('1', '2', '3', '4')


#accessing elements
print("2nd element: ", tup[1])

#immutable - can not be changed
#tup[2] = 20 #TypeError: 'tuple' object does not support item assignment

#if we re-assign tup = newtuple, it would be a reassignement, not updating existing tuple's values

#Also, we can not add/remove values from a tuple


#-------------
#slicing tuple from a list
ls = [1,2,3,4,5,6,7]
lsTup = tuple(ls[2:3])
print(lsTup) #(3,)
lsTup = tuple(ls[1:3])
print(lsTup) #(2,3)

lstup = (ls[1:3])
print(lstup) # return a list only [2, 3]


#Traversing tuple
tup = tuple(ls[:])
for a in tup:
    print(a)

print(tup.index(4)) #3 i.e. index value

#comparing tuples
tup1 = (1,2,3)
tup2 = (1,2,3)
if tup1 == tup2:
    print("equal")

tup1 = (1,2,3)
tup2 = (3,2,1)
if tup1 == tup2:
    print("Yup - equal") #doesn't work i.e. not equal

tup1 = (1,2,3)
tup2 = (1,2,3,4)
if tup1 in tup2:
    print("still equal") #doesn't work i.e. not equal


#concatenation

tup3 = tup1 + tup2
print(tup3) #(1, 2, 3, 1, 2, 3, 4)


#list and tuples
#tuples in a list
ls = [(1,3), (2,5), (3,6)]
print(ls) #[(1, 3), (2, 5), (3, 6)]
print(ls[0]) #(1,3)
t1 = ls[0] #tuple -> (1,3)
print(t1[1]) #3

#lists in a tuple
t1 = ([1,2,3], [4,5,6], [7,8,9])
print(t1)
# t1[0] = [0,1] #not allowed as tuple is immutable

 