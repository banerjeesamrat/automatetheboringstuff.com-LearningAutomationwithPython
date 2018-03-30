'''
    Python program to syntactically show the 4 rules to decide whether a variable is Local or Global.
    Rules :
    1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
    2. If there is a global statement for that variable in a function, it is a global variable.
    3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
    4. But if the variable is not used in an assignment statement, it is a global variable.

    Author : thegothamstak
    Date : 30th March 2018
'''
#Rule 2
def spam():
    global eggs
    eggs = 'spam'   #This is global

#Rule 3
def bacon():
    eggs = 'bacon'  #This is local
    print(eggs)

#Rule 4
def ham():
    print(eggs)     #This is global

#Rule 1
eggs = 'global'
print(eggs)

#Rule 2 output
spam()
print(eggs)

#Rule 3 output
bacon()

#Rule 4 output
ham()   #Output would be spam as the value of global variable eggs was changed by function spam()
