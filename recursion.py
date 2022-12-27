# problem 1

## This is to calculate power of 2
## Using two different approaches

#### Approach 1 : Using recursion

from unittest import result


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
#### Also, recursion might be risky & go into infinte loop if exit condition is not properly written. Hard to imagine at times too.


####### Still there can be use cases where recursion is preferable. 
#           e.g. when we think problem can be divided into smaller problems/soltions
#           or When we need quick solutions in terms of implementation
#           and in case of traversing a tree, recursion helps. Here, we may need to traverse tree back & forth.


# problem 2
## Calculate the factorial of a positive integer

## using recursion
def factorial_rec(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer only !" ##using assertion method as a conditional check
    result = 1
    if n in (0,1):
        return 1
    else:
        return n * factorial_rec(n-1)
n = 5
# n = -2 ## will report the error
# n = 1.5 ## will report the error as this is not an integer
print("Factorial of {0} is : ".format(n), factorial_rec(n))

## using iteration
def factorial_iteration(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer only !" ##using assertion method as a conditional check
    result = 1
    while n >= 1:
        result = result * n
        n -= 1
    return result

n = 6
print("Factorial of {0} is : ".format(n), factorial_rec(n))   
factorial_iteration


# problem 3
## Fibonacci series (e.g. 0, 1, ,1, 2, 3, 5, 8, 13, 21, 34, 55 i.e. sum of two previous numbers). In other words f(n) = f(n-1) + f(n-2)
#### ----> important point here is that result should return a series of numbers not a single value.
#### using recursion

def fib_rec(n):
    global result
    value = 0
    if n < 0:
        return
    elif n in [0,1]:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print("Nth number of the Fibonacci series for the given N is: ", fib_rec(6), "\n")
#to print the entire series
n = 6
for i in range(n+1):
    print(f"{i} Fibonacci term is: ",fib_rec(i))