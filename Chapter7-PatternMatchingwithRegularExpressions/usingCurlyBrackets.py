"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Matching Specific Repititions with Curly Brackets('{}')

"""
import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)
