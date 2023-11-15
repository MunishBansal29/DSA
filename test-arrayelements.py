# Python3 code to implement the above approach
from collections import Counter
 
# # function to calculate the no of operations
# def minOperations(a):
#     # a dictionary that stores the frequencies
#     mp = dict(Counter(a))

#     print(mp)
     
#     # variable to store the operations
#     operations = 0
     
#     # if occurrence > x, then the greedy move is
#     # to remove extra occurrences
#     for x in mp:
#         occurrences = mp[x]
         
#         if occurrences > x:
#             operations += occurrences - x
             
#         # else, you can remove all the occurrences of the no
#         # or add x until the occurrences
#         # of x are not equal to x itself.
#         elif occurrences < x:
#             operations += min(occurrences, x - occurrences)
#     # return the operations
#     return operations

# # array = [1,1,3,4,4,4]


def min_moves(arr):
    n = len(arr)
    mp = dict(Counter(arr))
    # for i in range(n):
    #     freq[min(n, arr[i])] += 1
    print(mp)
    moves = 0
    freq = 0
    for i in mp:
        freq = mp[i]
        if freq > i:            
            moves += freq - i
        elif freq < i:
            moves += min(freq, i-freq)
    return moves

# array = [1,1,3,4,4,4]
# array = [1,2,2,2,5,5,5,8]
array = [3,2,2,1,4,4,4,4,5,5, 5]
print(min_moves(array))