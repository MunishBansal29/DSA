print("\n")
print("Welcome to the DSA (Data Structure and Algorithm) course !")
print("\n")
print("This is a Python based course !!")
print("\n")


for i in range(10):
    print(i) #output : 0,1,2,3,4,5,6,7,8,9 i.e. 0 to 9 

for i in range(1, 10):
    print(i) #output : 1,2,3,4,5,6,7,8,9 i.e. 1 to 9 

for i in range(1,10,2): #2 -> step here
    print(i) #output: 1,3,5,7,9


for i in range(10,-1): #-1 - > in reverse
    print(i) #output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 (one less that -1, last value)

for i in range(10,-1, -1): #same as above i.e. when end is specfied as -ve, step has to be negative number too. Default is -1
    print("--\n",i) #output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 (one less that -1, last value)

str = "Hello"
print(str[1:-1]) #ell

## REVERSE STRING
str = "This is my string"
print(str[::-1]) #i.e. step if negative