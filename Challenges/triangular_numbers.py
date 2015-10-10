#!/usr/bin/env python
"""
Triangular Number

A triangular number is a number of dots it takes to make a triangular dot pattern.

Given the number of levels in a dot triangular pattern, return its triangular number.

1, 3, 6, 10 and 15 are triangular numbers for 1, 2, 3, 4 and 5 level triangles respectively.



Example:

For n = 2 the output should be 3.

[input] integer n

The number of levels in the triangle.
[output] integer

The number of dots in the triangle
"""

__author__ = 'pandeesh'

triangular_numbers = lambda n: n*(n+1)/2

#tests
print(triangular_numbers(3))
