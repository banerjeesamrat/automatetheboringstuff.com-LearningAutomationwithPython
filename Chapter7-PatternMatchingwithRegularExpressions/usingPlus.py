"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Matching One or More with Plus('+')

"""
import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batman')
print(mo2==None)
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
