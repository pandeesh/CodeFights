#!/usr/bin/env python

def bitCount(n):
    """
    no of active bits (1) in the binary form of the given no 'n'
    :param n: an integer
    :return: number of active bits in the binary representation of the given no 'n'
    """
    answer = 0
    while n > 0:
        if n & 1:
            answer += 1
        n >>= 1
    return answer

#test
print(bitCount(5))
print(bitCount(125))
