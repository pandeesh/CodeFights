#!/usr/bin/env pyhton
"""
If you write numbers from 1 to N next to each other, how many digits will be written?

Given number N, return the total number of digits written.

Examples

For N = 10 the answer should be 11, because [12345678910] has 11 digits.

[input] integer N

1 ≤ N ≤ 108.
[output] integer

The total number of digits.
"""

__author__ = 'pandeesh'

def CountingDigits(N):
  cnt = 0
  for i in range(1,N+1):
    cnt += len(str(i))
  return cnt

#tests
print(CountingDigits(22))

#alternative

def CountingDigitsAlternate(N):
  return sum([len(str(i)) for i in range(1,N+1)])

#tests
print(CountingDigitsAlternate(22))

