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

#another version
def RankOfElement_1(A, i):
   c = 0 
   for j in range(len(A)):
       if j<i and A[j] <= A[i] or j>i and A[j] < A[i]:
               c += 1
   return c
   

#another version
def RankOfElement_2(A, i):
   return sum(j<i and A[j] <= A[i] or j>i and A[j] < A[i] for j in range(len(A)))
   

#one more
def RankOfElement_3(A, i):
   return sum(j<i and A[j] <= A[i] or A[j] < A[i] for j in range(len(A)))
   
#tests
print(RankOfElement([3,2,3,4,1],0))


