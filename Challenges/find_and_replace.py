#!/usr/bin/env python

"""
ind all occurrences of the substring in the given string and replace them with another given string...
just for fun :)

Example:
findAndReplace("I love Codefights", "I", "We") = "We love Codefights"

[input] string originalString

The original string.
[input] string stringToFind

A string to find in the originalString.
[input] string stringToReplace

A string to replace with.
[output] string

The resulting string.
"""
def findAndReplace(o, s, r):
"""
o - original string
s - substitute
r - replace
"""
  return re.sub(s,r,o)
