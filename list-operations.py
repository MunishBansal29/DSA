#remove duplicate elements from the sorted list
from hashlib import new


ls = [1,2,3,4,4,5,6,7,7,8]

idx = 1 #0th element is anyway unique in itself

for i in range(1, len(ls)):
    if ls[i] != ls[i-1]:
        #unique value pair
        #let's keep on building/updating the list
        ls[idx] = ls[i]
        idx =+ 1 #so the idea is create(update the existing list with new indexes) the list where unique values found else move on

print(ls)


ls = [1,2,3,4,4,5,6,7,7,8]
ls_unique = set(ls)
print(ls_unique)


#convert string into list
str = "Hello World !"
ls = list(str)
print(ls) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', ' ', '!']

ls2 = str.split() #retruns a list
print(ls2)  #'Hello', 'World', '!']

#joint function is reverse of split()
strnew = ' '.join(ls2) #delimiter.join #delimiter could be a var carrying any char/delimter. This delimter will be the joining element joining all the values of the list to return a concatenated string value
print(strnew) #retruns string "Hello World !"



data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
    print(v)
    for row in m:
        print(row)
        for element in row:
            if v < element: v = element #i.e. get the max (>1)
 
    return v
print(fun(data[0]))

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1 # this is making list2 referencing to the same list1
fruit_list3 = fruit_list1[:] #this is not referencing, but coping the data to a new list
#print(fruit_list3)
 
fruit_list2[0] = 'Guava' #['Guava', 'Berry', 'Cherry', 'Papaya'] #this is changing list1 too.........
fruit_list3[1] = 'Kiwi' #['Apple', 'Kiwi', 'Cherry', 'Papaya']
 
print(fruit_list1) 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3): #ls get one list at a time, in three iterations
    #print(ls)
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

newlist = [1,2,5,6,7]
newlist = newlist + [8,9] #joins the list
print(newlist)  #[1, 2, 5, 6, 7, 8, 9]

newlist[2], newlist[3] = (3,4) #will update list at given indexes
print(newlist)

ls=[10,11]
newlist.append(ls)
print(newlist) #[1, 2, 3, 4, 7, 8, 9, [10, 11]], appended as a nested list. if we append just a value, it will be part of the given list as an usual value



ls=[5,6,7]
ls_updated = ls * 3
print(ls_updated) #[5, 6, 7, 5, 6, 7, 5, 6, 7] i.e. will repeat the list 3 times

ls=[5,6,7, 8]
ls[1], ls[2] = 1, 3
print(ls) # [5, 1, 3, 8]

ls=[5,6,7]
ls_updated = [i * 3 for i in ls]
print(ls_updated) #[15, 18, 21] i.e. multiple each element by 3

#sorting
ls = [3,2,5,1,8,7,9,10]
# print(ls.sort()) #sort function doesn't return anything but sorts the input list thereitself
ls.sort()
print(ls) #[1, 2, 3, 5, 7, 8, 9, 10]

#sorted function?
ls = [3,2,5,1,8,7,9,10]
print(sorted(ls)) #[1, 2, 3, 5, 7, 8, 9, 10]. ls here itself is not changed, it needs to be received into another one as sorted list

#sorted allows further conditions to be applied etc.
ls_sorted = sorted(ls, reverse=True)
print(ls_sorted) #[10, 9, 8, 7, 5, 3, 2, 1]

ls = [3,2,5,1,8,7,9,10]
ls_sorted = sorted([i for i in ls if i>3]) ##->>>>>Good one
print(ls_sorted) [5, 7, 8, 9, 10]




