#!/usr/bin/env python

"""
For Array = ["codefights","fightscode"] the output should be "YES".
For Array = ["code", "odec"] the output should be "YES".
For Array = ["butter", "tterub"] the output should be "NO".

In the second example if you rotate s2 clockwise, 'c' will move in front of the modified string, so it will become code. Thus the answer is "YES".

[input] array.string Array

An array of length 2, 1 ≤ Array[i] ≤ 100. Each character is a lowercase Latin letter.
[output] string

"YES" or "NO".
"""

#using itertools.permutations
def stringRotation(A):
   if A[1] in [''.join(p) for p in itertools.permutations(A[0])]:
      return "YES"
   return "NO"

#without using itertools.permutations
def stringRotation_1(A):
    if len(A[0]) == len(A[1]) and (A[0] + A[1]).find(A[1]):
       return "YES"
    return "NO"
    
#tests

A = ["codefights","fightscode"]
print(stringRotation_1(A))
print(stringRotation(A))
