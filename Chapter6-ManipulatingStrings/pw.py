#! /usr/bin/python3.5
# First Project of An Insecure Password Locker Program
# Author: Samrat Banerjee
# Date: 15-03-2018

# The dictionary will be the data structure that organizes your account and password data.

# Step1-Program Design and Data Structures

PASSWORDS={'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# Step2-Handle Command Line Arguments

import sys,pyperclip

if len(sys.argv)<2:
 print('Usage: python pw.py[account]-copy account password')
 sys.exit()

account=sys.argv[1]	# first command line arg is the account name

# Step3-Copy the Right Password

if account in PASSWORDS:
 pyperclip.copy(PASSWORDS[account])
 print('Password for '+account+' copied to clipboard')
else:
 print('There is no account named '+account)


