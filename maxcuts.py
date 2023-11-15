# Given an integer N denoting the Length of a line segment. You need to cut the line segment in such a way that the cut length of a line segment 
# each time is either x , y or z. Here x, y, and z are integers.
# After performing all the cut operations, your total number of cut segments must be maximum

def maximizeTheCuts(n,x,y,z):
        #code here
        ls = sorted([x, y, z])
        cut = 0
        for i in ls:
            
            seg = int(n/i)
            rem = n%i
            
            if rem == x or rem == y or rem == z:
                seg += 1
            cut = max(seg, cut)
            
        return cut

print(maximizeTheCuts(5,5,2,3))