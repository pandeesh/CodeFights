#!/usr/bin/env python

"""
Given two strings, return "YES" if their encryption is the same, or "NO" otherwise.

[input] string FirstString

The first string to be encrypted.
[input] string SecondString

The second string to be encrypted.
[output] string

"YES" if encryption is the same, "NO" otherwise.
"""

__author__ = 'pandeesh'

def SameEncryption(FirstString, SecondString):
   ffl = FirstString[0]
   fll = FirstString[-1]
   flc = len(FirstString)-2
   sfl = SecondString[0]
   sll = SecondString[-1]
   slc = len(SecondString)-2
   if ffl+str(digitalroot(flc))+fll == sfl+str(digitalroot(slc))+sll:
       return 'YES'
   else:
       return 'NO'

def digitalroot(n):
  if len(str(n)) == 1:
    return n
  else:
    j = 0
    for i in range(0,len(str(n))):
        j += int((str(n))[i])
    return digitalroot(j)

#tests
x = SameEncryption('Ehgz','E12z')
print(x)
