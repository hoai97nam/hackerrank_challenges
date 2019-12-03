'''
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

def is_multiple(n,m):
    if m % n == 0:
        return True
    else:
        return False

"""
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

from math import *
def is_even(k):
    _, b = divmod(k, 2)
    if b == 0:
        return True
    return False

"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(s):
    min = max = s[0]
    for a in s:
        if min >= a:
            min = a
        if max <= a:
            max = a
    return min, max
# minmax([1,2,3,4,5,6])

"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def sumSquare(n):
    s = 0
    for i in range(n):
        s = s + pow(i, 2)
    return s
# a = sumSquare(10)
# print(a)

"""
Give a single command that computes the sum from Exercise R-1.4, 
relying on Python’s comprehension syntax and the built-in sum function.
"""

"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def sumOddSquare(n):
    s = 0
    for i in range(n):
        if i%2==1:
            s = s + pow(i, 2)
    return s
# a = sumOddSquare(10)
# print(a)

"""
Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function.
"""
def sumOddSquare1(n):
    s = []
    for i in range(n):
        if i%2==1:
            s.append(pow(i, 2))
    return sum(s)
# a = sumOddSquare1(10)
# print(a)

"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for
index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""
# k = range(-5,0,1)
# j = range(5)
# m='hello'
# for a in k:
#     print(m[a])
# for b in j:
#     print(m[b])

"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

# range(50,90)

"""
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""
# range(8,-10,-2)

"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
"""
def list():
    a = []
    for i in range(9):
        a.append(int(pow(2,i)))
    print (a)
# list()

"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a 
more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
import random
def myChoice():
    print(random.randrange(1,10,1))
# myChoice()

"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

def pseudoList():
    l = []
    for i in range(5):
        l.append(random.randint(1,10))
    for i in range(5):
        l[i] = -l[i]
    print(l)

# pseudoList()
"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def checking(s):
    silo = []
    for i in s:
        if len(silo) == 0:
            silo.append(i)
        if i in silo:
            pass
        else:
            silo.append(i)
    if len(silo) == len(s):
        return True
    return False

# print(checking([1,2,3,4]))

"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)
"""

def checking(s):
    silo = []
    for i in s:
        if len(silo) == 0:
            silo.append(i)
        if i in silo:
            pass
        else:
            silo.append(i)
    for i in silo:
        s.pop(s.index(i))
    return (s)

# print(checking([1,2,3,4,1]))
