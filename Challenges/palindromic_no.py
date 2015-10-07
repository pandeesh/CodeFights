#!/usr/bin/env python
"""
You're given a digit N.

Your task is to return "1234...N...4321".

Example:

For N = 5, the output is "123454321".
For N = 8, the output is "123456787654321".

[input] integer N

0 < N < 10
[output] string
"""

def Palindromic_Number(N):
    s = ''
    for i in range(1,N):
        s = s + str(i)
    return s + str(N) + s[::-1]

#tests
print(Palindromic_Number(5))
