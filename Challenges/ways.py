#!/usr/bin/env python
"""
Let W(n, m) be the number of ways to divide a set of n things into m nonempty subsets. For example, there are seven ways to split a four-element set into two parts: {1, 2, 3} ∪ {4}, {1, 2, 4} ∪ {3}, {1, 3, 4} ∪ {2}, {2, 3, 4} ∪ {1}, {1, 2} ∪ {3, 4}, {1, 3} ∪ {2, 4}, {1, 4} ∪ {2, 3}.

Given integers n and m, find W(n, m) % 2.

Example:

W(4, 2) % 2 = 1

[input] integer n

[input] integer m

[output] integer

W(n, m) % 2

(After an analysis, i found that the generic formual is (n * m) - 1 when n != m)
"""

def ways(n, m):
  return 1 if n == m or m == 1 else (( n * m ) - 1 ) % 2
  
#tests
print(ways(3,2))
