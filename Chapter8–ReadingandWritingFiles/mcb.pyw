#! /usr/bin/python3.5

"""

Author: Samrat Banerjee
Dated: 28/05/2018
Description: PROJECT- Saves and loads pieces of text to the clipboard.

py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
py.exe mcb.pyw list - Loads all keywords to clipboard.

"""

import shelve, pyperclip, sys

mcbShelf=shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
#List keywords and load content
elif len(sys.argv)==2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
