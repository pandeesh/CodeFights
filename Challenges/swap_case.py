#!/usr/bin/env python
"""
Your task is to swap cases of the letters in the given string, i.e. convert lowercase letters to uppercase and vice versa.

Example

SC("54236cdsckjbjk!#AADC") = "54236CDSCKJBJK!#aadc"

[input] string s

[output] string

"""
def SC(s):
   n = []
   for i in s:
      if i.isalpha():
         if i.isupper():
             n.append(i.lower())
         else:
             n.append(i.upper())
      else:
         n.append(i)
   return ''.join(n)

#test
print(SC("54236cdsckjbjk!#AADC"))
