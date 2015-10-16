#!/usr/bin/env python
"""
sorry, but for some reason I am unable to set the output to float. So this challenge is kind of incomplete and easy (that was a hint).

Example:

nroot(8, 3) = 2

Since 23 = 8.

[input] integer num

The number which root should be calculated.
[input] integer root

The degree of the root.
[output] integer

The answer.
"""
def nroot(n, r):
   for i in range(n+1):
      if i ** r == n:
        return i
        
#test
print(nroot(8,3))
