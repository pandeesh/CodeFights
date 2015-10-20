#!/usr/bin/env python
"""
There are a lot of species on planet Tazenda, and we know there is a dominant one. The dominant species constitute more than half of the total living creatures on the planet.

You know that each species has a unique integer number, their ID. Each creature has the ID of the species it belongs to. So, tell me, what ID the dominant species have?

Example:

Dominant_species([1,2,1,3,3,1,0,1,1,9,1]) = 1

[input] array.integer A

The "species number" of each creature on the planet.
[output] integer

The dominant species number.

(collections.Counter() makes it simple!)
"""

from collections import Counter

def Dominant_species(A):
   return Counter(A).most_common(1)[0][0]

#tests
print(Dominant_species([1,2,1,3,3,1,0,1,1,9,1]))
