#!/usr/bin/env python

"""
https://codefights.com/challenge/ohGqHAbKxP3q6Yezk
Given two integers a and b, return the sum of the numerator and the denominator of the reduced fraction a/b.

Example:

Fraction(2, 4) = 3, since
2/4 = 1/2 => 1 + 2 = 3.
Fraction(10, 100) = 11, since
10/100 = 1/10 => 1 + 10 = 11.
Fraction(5, 5) = 2, since
5/5 = 1/1 => 1 + 1 = 2.
[input] integer a

The numerator, 1 ≤ a ≤ 2000.
[input] integer b

The denominator, 1 ≤ b ≤ 2000.
[output] integer

The sum of the numerator and the denominator of the reduces fraction.
"""
def Fraction(a, b):
  if a == b:
    return 2
  c = [] 
  for i in range(2,max(a,b)):
    if a % i == 0 and b % i == 0:
      c.append(i)
  if c:
    return (a/max(c)) + (b/max(c))
  return a + b

#tests
print(Fraction(90,120))
