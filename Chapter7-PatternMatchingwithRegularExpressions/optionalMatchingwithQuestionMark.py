"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Optional Matching with Question Mark('?')

"""
import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
