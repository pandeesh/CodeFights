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
import cProfile
import pstats

def sumofoddnumbers(a, b):

    start_pos = math.ceil( a / 2 )
    end_pos =  math.floor( b / 2 )

    return end_pos ** 2 - start_pos ** 2

#tests
x = sumofoddnumbers(3,5)
print(x)

x = sumofoddnumbers(30,4090)
print(x)

#profiler test, need to generalize this as an externla module which can be invoked from any other programs

profiler = cProfile.Profile()
profiler.runcall(sumofoddnumbers)

stat = pstats.Stats(profiler)
stat.strip_dirs()
stat.sort_stats('cumulative')
stat.print_stats()

"""
/usr/local/bin/python3 /Users/pandeesh/PycharmProjects/untitled/sumofoddnos.py
1923016
         4 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 sumofoddnos.py:7(sumofoddnumbers)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
        1    0.000    0.000    0.000    0.000 {built-in method math.floor}
"""
