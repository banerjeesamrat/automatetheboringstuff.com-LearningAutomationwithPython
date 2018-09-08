#! /usr/bin/python3.5

"""

Author: Samrat Banerjee
Dated: 08/09/2018
Description: Project: A simple countdown script.

"""

import time, subprocess,webbrowser

timeLeft=60

while timeLeft>0:
    print(timeLeft,end=' ')
    time.sleep(1)
    timeLeft=timeLeft-1

    # At the end of the countdown, play a sound file.
    webbrowser.open("https://www.rediff.com/")
