#! /usr/bin/python3.5


"""

Author: Samrat Banerjee
Dated: 10/09/2018
Description: Project: Displays the mouse cursor's current position.

"""

import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


except KeyboardInterrupt:
    print('\nDone.')
