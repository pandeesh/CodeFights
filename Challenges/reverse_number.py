#!/usr/bin/env python

"""
Find the reversed number from the given one.

Example:
For n = 6587 the answer is 7856.
Note:
For n = 20 the answer is 2.

[input] integer n

[output] integer

"""
__author__ = 'pandeesh'

def reverse_number(n):
    if str(n)[-1] == 0:
        return int(str(n)[::-2])
    return int(str(n)[::-1])

#tests
x = reverse_number(1213543424)
print(x)
