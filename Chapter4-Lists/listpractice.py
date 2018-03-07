"""

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list
to the function would return
'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.

"""

spam = ['apples', 'bananas', 'tofu', 'cats']



def listpractice(spam):
    if len(spam)==0:
        return None
    elif len(spam)==1:
        return(spam[0])
    else:
        return(', '.join(spam[:-1]+['and '+spam[-1]]))


print(listpractice(spam))
