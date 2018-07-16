"""

Author: Samrat Banerjee
Dated: 14/07/2018
Description: Getting Traceback as a String

"""

def spam():
    bacon()
def bacon():
    raise Exception('This is an error message.')

spam()
