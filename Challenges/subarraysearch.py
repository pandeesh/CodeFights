#!/usr/bin/env python
"""
Determine if the given subarray is a subarray of the given array.
A string is a subarray of another string if the first string is not longer than the second, 
and all its letters are present in the second string in the exact same order, 
but not necessarily consecutive. Cases of the letters do not matter.

Example:

subarraysearch("ABCdefgh", "bCf) = true
subarraysearch("ABCdefgh", 'i') = false

[input] string array

Input string, 2 < array < 10.
[input] string subarray

A subarray.
[output] boolean

true if subarray is a subarray of the array, false otherwise.
"""

def subarraysearch(a, s):
  if len(a) <= len(s):
    return False
  else:
    r = []
    a = a.upper()
    s = s.upper()
    for i in range(len(s)):
       if s[i] in list(a):
          r.append(s[i])
    if list(s) == r:
       return True
    return False
   
#tests
print(subarraysearch("ABCdefgh", "bCf"))
print(subarraysearch("ABCdefgh", 'i'))
