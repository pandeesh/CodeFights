#!/usr/bin/env python
"""
Example
For a = 3 and b = 5 the output should be 0.
For a = 3006 and b = 4090 the output should be 1923016.

Note
If you don't want to read the text below, maybe your code won't pass time and memory limits. ;)

[input] integer a

The first integer, -1 < a < 1e8.
[input] integer b

The second integer, 0 < b < 1e8 + 1.
[output] integer

Return the answer modulo 10000007
"""

__author__ = 'pandeesh'

import math

def sumofoddnumbers(a, b):

    start_pos = math.ceil( a / 2 )
    end_pos =  math.floor( b / 2 )

    return end_pos ** 2 - start_pos ** 2

#tests
x = sumofoddnumbers(3,5)
print(x)

x = sumofoddnumbers(30,4090)
print(x)
