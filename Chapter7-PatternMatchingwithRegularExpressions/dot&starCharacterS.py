"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Dot(Wildcard) Character

"""
import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Using .*(Greedy)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# Non-greedy .*
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())


noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# Matching newlines with dot character
NewlineRegex = re.compile('.*',re.DOTALL)
print(NewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
