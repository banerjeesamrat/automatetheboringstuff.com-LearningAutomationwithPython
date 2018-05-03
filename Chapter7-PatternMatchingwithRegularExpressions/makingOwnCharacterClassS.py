"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Making own character classes using square brackets('[]')

"""
import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
