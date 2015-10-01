#!/usr/bin/env python

"""
A number is called palindrome_prime if it is palindromic and it is prime. We assume a number is palindromic if it reads the same backward or forward.
Here is the problem: Given a positive integer N, your job is to find out whether it is a palindrome_prime. If it is a palindrome_prime, please return true. Otherwise please return false.

Note:
1 is not a prime.

[input] integer N

A positive number N (1 ≤ N ≤ 1,000,000).
[output] boolean

Please output the answer.
"""

__author__ = 'pandeesh'

def palindrome_prime(N):
    
    return (str(N) == str(N)[::-1]) and all(N % i for i in range(2, N)) and N != 1

#tests

X = palindrome_prime(131)
print(X)

X = palindrome_prime(1)
print(X)
