from urllib import robotparser


def rotateme(arr):
    l = len(arr) // 2
    index = len(arr) - 1
    for i in range(l):
        arr[i], arr[index] = arr[index], arr[i]
        l -= 1
        index -= 1
    return arr

arr = [3,4,6,1,7,8,10]
print(rotateme(arr))


## Shift the numbers in an array by the given position
# https://github.com/Dineshkarthik/codility-training/blob/master/Lesson%2002%20-%20Arrays/cyclicrotation.py
def rorate(arr, k):
    count = len(arr)    
    #print(temp_arr)
    temp_arr = [None] * count    
    for i in range(0, count):
        #if i < count-1:
            temp_arr[(i + k)%count] = arr[i]
        #else:
        #    temp_arr[0] = arr[i]
    #print(arr)    
    return temp_arr

arr = []
print(rorate(arr, 3))
