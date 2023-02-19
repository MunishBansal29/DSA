"""You are given a description of a two-lane road in which two strings, L1 and L2, represent the first and the second lane. Each lane consists of N segments of equal length.

The K-th segment of the first lane is represented by L1[K], and the K-th segment of the second lane is represented by L2[K], where “.” denotes a smooth segment of road, and “x” denotes a segment that contains potholes.

Cars can drive over segments with potholes, but it is uncomfortable for passengers. Therefore, a project to repair as many potholes as possible was submitted. At most one contiguous region of each lane may be repaired at a time. The region is closed to traffic while it is under repair.

How many road segments with potholes can be repaired given that the road must be kept open?

For example, if L1 = “..xx.x.” and L2 = “x.x.x..”, the maximum number of potholes we can repair is 4. See Figure 1 for an explanation.
"""

def max_repairable_potholes(L1, L2):
    start, end = 0, 0
    max_potholes = 0
    potholes = 0
    for i in range(len(L1)):
        if L1[i] == 'x' or L2[i] == 'x':
            potholes += 1
        else:
            while potholes > 1:
                if L1[start] == 'x':
                    potholes -= 1
                start += 1
            max_potholes = max(max_potholes, potholes)
            end = i + 1
            potholes = 0
    return max_potholes




#consideration: both the strings are of the same length
# '.' -> clear road, 'x' -> pothole
strL1 = "..xx..."
strL2 = "x....x."

##convert strings into lists
L1 = []
L2 = []
L1[:] = strL1
L2[:] = strL2

print(L1,L2)

print(max_repairable_potholes(strL1, strL2))  



