#!/usr/bin/env python

"""
Rank of Array Element

Given an array A, find the rank of the element at the ith position.

The rank of the A[i] is a value equal to the number of elements less than or equal to A[i] standing before A[i], plus the number of elements less than A[i] standing after A[i].

[input] array.integer A

An array of integers, |A| < 15.
[input] integer i

Index of the element whose rank is to be found.
[output] integer

Rank of the element at the ith position.
"""

def RankOfElement(A, i):
   cnt =0
   for j in range(i):
       if A[j] <= A[i]:
        cnt += 1
   for k in range(i+1,len(A)):
       if A[k] < A[i]:
        cnt += 1
   return cnt
   
#tests
print(RankOfElement([3,2,3,4,1],0))
