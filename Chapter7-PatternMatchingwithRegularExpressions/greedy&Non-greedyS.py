"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Greedy & Non-Greedy Matching

"""
import re

# Matching in Python is by default greedy giving the longest possible string
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# Adding a question mark after curly braces makes a non-greedy match giving a shorter string
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
