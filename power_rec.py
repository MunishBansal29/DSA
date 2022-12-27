## This is to calculate power of 2
## Using two different approaches

#### Approach 1 : Using recursion

def poweroftwp (n):
    if n == 0:
        return 1
    else:
        power = poweroftwp(n-1)
        return power * 2

print(poweroftwp(5))

#### Approach 2 : using iteration

def poweriteration(n):
    value = 1
    while n >= 1:
         value = 2 * value
         n -= 1
    return value

print(poweriteration(5))


#### Summary : Iteration (while loop) is more space & time efficient, at least in such scenarios.
#### In case of recurison (approach 1), stack memory is used to track the function (same) calls, and hence takes more memory as well as time.