#Dictionary is unordered, changeable and indexed (on keys)
from asyncio import new_event_loop
from hashlib import new
from collections import Counter
from itertools import count


myDict = dict() #empty dictionary
print(myDict) # {} 

#OR

myOtherDict = {}
print(myOtherDict)

newDict = {"Name":"John", "Age":55, "Salary":75.5}
print(newDict) #order is not guranteed, and hence not accessible via sequence indexes like 0,1,2 but with keys

print(newDict["Salary"])

otherDict = {"ID":1234, "Id": 2345}
print(otherDict) #works fine

otherDupDict = {"ID":1234, "ID": 2345}
print(otherDupDict) #Second value overwrites the first one with the same key i.e. output = {'ID': 2345}
#this happens because Hash value of the Key (as dictionaries are stored via Hash table storing key & corresponding indexes to the arrays/lists which actually store the values)
#and since key is the same, hash generated of the key is the same and hence mapped to the same index (overwritten by the latest one) into the array/list

#update value
otherDict["Salary"] = 80 #Key is case sensitive, if it does not match it will be a new key-value created/added
print(otherDict)

otherDict["Org"] = "Natwest" #added as a new key-value O(1)
print(otherDict)

#traversing - default works on keys
for key in otherDict:         #time complexity O(n)
    print(key, otherDict[key]) 

#travsering using values
for value in otherDict.values():
    print(value)

#searching element - same as above

##### all(dict) -> returns TRUE if all the VALUES in the given dict is true or empty
 
#### any(dict) -> returns TRUE if Any VALUE in the given dict is true


#Delete an element
print(newDict.pop("Age")) #By key, returns the value removed/poped

#adding it back
newDict["Age"] = 55

#popitem
#newDict.popitem() #removes any arbitrary item, and retruns key & value of the deleted item

#clear() - to remove all the items i.e. makes it empty
#newDict.clear()

#del newDict -> will delete the dict, no more accessible

#Copy method - creates a duplicate copy of the dict
copyDict = newDict.copy()

#another way to dynamically create a dictionary
dynamicDict = {}.fromkeys(["ID", "Name", "Address"], "None") #only one value (same) for the keys to be specified
print(dynamicDict) #{'ID': 'None', 'Name': 'None', 'Address': 'None'}
#So, basically creating a skelton dictionary for further manipulations

#get function - retrun the value of the given key if it exists, else we can return value of choice.
print(dynamicDict.get("Phone", 1001)) #output 1001, as the key "Phone" doesn't exist in the given dictionary

print(dynamicDict.items()) #dict_items([('ID', 'None'), ('Name', 'None'), ('Address', 'None')]) i.e. returns tuples

# for item in dynamicDict.items():
#     print(i

print(dynamicDict.keys()) #dict_keys(['ID', 'Name', 'Address'])

if "Name" in dynamicDict.keys():
    print("Key exists !")


#oneDict.update(otherDict) -> updates from otherDict to oneDict, if keys exist then update else inserted

# Mapping key values to Dictionary
# Using dictionary comprehension
  
# initializing list
test_list = [{'name' : 'Manjeet', 'age' : 23}, 
             {'name' : 'Akshat',  'age' : 22},
             {'name' : 'Nikhil', 'age' : 21}]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Mapping key values to Dictionary
# Using dictionary comprehension
res = {sub['name'] : sub['age'] for sub in test_list}
  
# printing result 
print("The flattened dictionary is : " + str(dict(res))) 


#quering based upon key or value
ls = [1,1,2,3,6,7,3,7,8,9,1]
dict = Counter(ls)
print(dict) #Counter({1: 3, 3: 2, 7: 2, 2: 1, 6: 1, 8: 1, 9: 1})
print(dict.get(3)) #gives the value at the specified key
max_key = max(dict) #will give the max key

max_val_key = max(dict, key = dict.get) #this will give KEY where value is the max (in this case, max value is 3 for key = 1, hence result is 1
print(dict[max_val_key]) #prints the value 3 where value is max.





















