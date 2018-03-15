#! /usr/bin/python3.5

# Second Project that adds Wikipedia bullet points to the start of each line of text on the clipboard.
# Author : Samrat Banerjee
# Date : 15-03-2018

# Steps in this program are combined

import pyperclip

text=pyperclip.paste()

# Separate lines and stars

lines=text.split('\n')
for i in range(len(lines)):	#loop through all indexes in the "lines" list
 lines[i]='* '+lines[i]		# add star to each string in "lines" list

text='\n'.join(lines)

pyperclip.copy(text)
