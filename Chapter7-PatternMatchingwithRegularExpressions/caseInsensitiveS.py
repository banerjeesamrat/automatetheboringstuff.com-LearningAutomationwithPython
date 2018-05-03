"""

Author: Samrat Banerjee
Dated: 04/05/2018
Description: Case-insensitive matching

"""
import re

robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
