"""

Author: Samrat Banerjee
Dated: 03/05/2018
Description: Learning regular expressions through isPhoneNumber() function now modified

"""

import re
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# putting an r before the first quote of the string value, you can mark the string as a raw string,
# which does not escape characters. This is done to avoid multiple backslashes

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
