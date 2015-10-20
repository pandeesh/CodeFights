#!/usr/bin/env python
"""
You're given a number N. Find the smallest number greater than N which has the same number of active bits in it (i.e. the same number of 1 in binary representation).

Examples:

For N = 1 the output should be 2 (they both have 1 active bit)
For N = 3 the output should be 5 (they both have 2 active bits)
[input] integer N

1 ≤ n ≤ 109.
[output] integer
"""
def nextNumber(N):
    c = bin(N).count('1')
    N += 1
    while c != bin(N).count('1'):
        N += 1
    return N

#tests
print(nextNumber(1))
print(nextNumber(2))
