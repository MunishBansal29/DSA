from abc import update_abstractmethods
from tkinter.messagebox import NO
from turtle import up


# A = [[1,2,3], [2,3,4], [4,5,6]]
A=[[1,2,2], [3,1,4]]
A=[[4,3], [5,5], [6,2]]
A = [[1,1,5,2,3], [4,5,6,4,3], [9,4,4,1,5]]
A = [[1,2,3,4], [1,2,3,4], [5,6,7,8]]
# print(A[:][0])
#print(len(A[0]))
def NoOfDoctors(ls):
    doc = dict()
    for i in range(len(A)):
        for j in range(len(A[0])):
            #if i != j:
            if A[i][j] in doc.keys():
                doc[A[i][j]] += 1
            else:
                doc[A[i][j]] = 1    
    count = 0    
    for key in doc:
        if doc[key] > 1:
            count += 1

    ls = [x for x in doc.values() if x > 1]
    print(doc)
    print(ls, len(ls))
    return count

print(NoOfDoctors(A))