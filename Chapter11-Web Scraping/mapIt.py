#! /usr/bin/python3.5

"""

Author: Samrat Banerjee
Dated: 17/07/2018
Description: Project: Launches a map in the browser using an address from the command line or clipboard.

"""

import webbrowser,sys,pyperclip

if len(sys.argv)>1:
    # Get address from command line
    address=''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
