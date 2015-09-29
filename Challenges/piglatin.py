#!/usr/bin/env python

"""
Here’s how it works.

If a word starts with a vowel ('a', 'e', 'i', 'o', 'u', or 'y'), just append "way" to the end of the word.

If a word starts with a consonant (a letter that's not a vowel), move all consonants leading up to the first vowel to the end of the word and add an "ay" at the very end.

Given a word, translate it into Pig Latin.

Example:

For word = "amazing" the answer should be "amazingway".
For word = "codefights" the answer should be "odefightscay".
For word = "flywhy" the answer should be "ywhyflay".

[input] string word

A word to be converted into pig-latin. It is guaranteed that it consists of lower-case latin letters only, and there is at least one vowel in it. 3 < word.length < 20.
[output] string

The input word converted into pig-latin.

"""

__author__ = 'pandeesh'

def piglatin(word):
    vowels = ['a','e','i','o','u','y']

    if word[0] in vowels:
        return word + 'way'
    else:
        idx = [i for i, v in enumerate(list(word)) if v in vowels]
        return word[idx[0]:] + word[:idx[0]] + 'ay'


#tests
res = piglatin('amazing')
print(res)

res = piglatin('codefights')
print(res)

res = piglatin('flywhy')
print(res)
