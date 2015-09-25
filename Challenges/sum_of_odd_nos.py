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

def sumofoddnumbers(a, b):
    j = 0
    for i in range(a,b)[1:]:
      if i%2 == 0:
        continue
      else:
        j += i
    return j

#tests
x = sumofoddnumbers(30,4090)
print(x)
