#!/usr/bin/emv python

"""
    The electronic color code is used to indicate the values or ratings of electronic components, usually for resistors, but also for capacitors, inductors, and others.

You are given an array of strings containing the color code of a resistor. Identify its resistance and tolerance.

Refer to the table here for the conversion from color codes to number: https://en.wikipedia.org/wiki/Electronic_color_code#Resistor_color-coding

The first three strings will be in the range from "black" to "white" (refer to the link).
The last string may be "gold", "silver" or none ("").

The 1st color represents the 1st digit.
The 2nd color represents the 2nd digit.
The 3rd color represents the decimal multiplier (power of 10).
The 4th color represents its tolerance (5%, 10% or 20%).

Example:

Ohms(["orange","red","yellow",""]) = ["320000","20%"]
orange -> 3
red -> 2
yellow -> 104 = 10000
"" (none) -> 20%

Ohms(["brown","black","black","gold"]) = ["10","5%"]
brown -> 1
black -> 0
black -> 100 = 1
gold -> 5%

Note: in the test cases the color "gray" is used, not "grey".

[input] array.string colors

An array of strings with a length of 4.
[output] array.string

An array of strings with a length of 2.

"""
def Ohms(c):

   d = { 'orange':3,'red':2,'yellow':4,'brown':1,'black':0,
        'green':5, 'silver':10, 'gold':5, 'white':9,'blue':6,
        'violet':7,'gray':8 }

   if not c[3]:
      d[c[3]] = 20

   return [str(int(str(d[c[0]]) + str(d[c[1]])) * (10 ** d[c[2]])),
          str(d[c[3]]) + '%']

   
#tests
print(Ohms(["orange","red","yellow",""]))

print(Ohms(["brown","black","black","gold"]))
