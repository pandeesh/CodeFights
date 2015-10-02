#!/usr/bin/env python
"""
Given a string, reverse it omitting all non-alphabetic characters.

Example:

For str1 = "krishan" the output should be "nahsirk".
For str1 = "ultr53o?n" the output should be "nortlu".
[input] string str1

[output] string


"""
__author__ = 'pandeesh'

import re

def reverse_string(str1):
  """ using re module """
  return re.sub('[\W\d]', '', str1[::-1])

def reverse_string_alternate(str1):
  """ without using re module"""
  return "".join([x for x in str1[::-1] if x.isalpha()])


#tests
print(reverse_string("pand1eesh123@"))
print(reverse_string("pandeesh"))
print(reverse_string_alternate("pandees1h2"))
