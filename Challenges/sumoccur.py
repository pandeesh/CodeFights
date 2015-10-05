#!/usr/bin/env python

"""
Return the sum of products of each number in the given array and the number of times it occurs there.

Example:

For A = [ 2 , 2 , 2 , 4 , 4 , 5] the output should be 2 * 3 + 4 * 2 + 5 * 1 = 19

[input] array.integer A

1 ≤ |A| ≤ 105, 1 ≤ A[i] ≤ 9.
[output] integer
"""

"""
It's pretty straightforward, no need of counter
"""
def sumOccur(A):
  return sum(A)
  
#below solutions would work, but not necessary for this case
from collections import Counter

def sumOccur1(A):
  counter = Counter(A)
  sum = 0
  for e, n in counter.most_common():
    sum += e * n
  return sum
  
  
#Alternative
def sumOccur2(A):
   return sum([ e * n for e,n in Counter(A).most_common()])


#tests
print(sumOccur([1, 1, 1, 2, 2, 3]))
print(sumOccur1([2, 3, 4, 2, 2, 3]))
print(sumOccur2([2, 3, 4, 2, 2, 3]))


