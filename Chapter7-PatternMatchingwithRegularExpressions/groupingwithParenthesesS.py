"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: More Pattern matching-Grouping with Parentheses(Separating area code from the phone number)

"""
import re

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1)) # First Group
print(mo.group(2)) # Second Group
print(mo.group(0)) # Entire matched text
print(mo.group())  # Entire matched text
print(mo.groups()) # Multiple groups at once
areaCode, mainNumber=mo.groups()
print(areaCode)
print(mainNumber)

# When Parentheses have to be used in regular expressions

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
