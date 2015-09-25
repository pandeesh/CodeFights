#!/usr/bin/env python

"""
https://codefights.com/challenge/7HtSqXrR2fAugzeJZ

A digital root is a positive single-digit integer which is obtained by adding digits of the initial number and repeating this process while it has more than one digit.

Given a positive integer as a string, return its digital root.

Example

For n = "24" the result is
2 + 4 ==> 6.
For n = "39" the result is
3 + 9 ==> 12 ==> 1 + 2 ==> 3.
For n = "999" the result is
9 + 9 + 9 ==> 27 ==> 2 + 7 ==> 9.
[input] string n

The input number, can contain up to 100 digits, n > 0
[output] integer

The digital root.

"""

__author__ = 'pandeesh'


def digitalroot(n):
  if len(str(n)) != 1:
    j = 0
    for i in range(0,len(str(n))):
        j += int((str(n))[i])
    digitalroot(j)
  else:
    print(n)

digitalroot(345)
