'''
	To use the list methods : index(), append(), insert(), remove(), sort()

	Author : thegothamstak
	Date : 3rd May 2018
'''
#	Creating a list
pets = ['dog','cat','horse']

#	Using index() method

indexOfDog = pets.index('dog')
print('Index of dogs will be displayed using index() method,')
print(indexOfDog)

#	Using append() method

pets.append('cow')
print('cow are appened to the list using append() method,')
print(pets)

#	Using insert() method

pets.insert(1, 'buffalo')
print('buffalo will be inserted at index 1 using insert() method,')
print(pets)

#	Using remove() method

pets.remove('buffalo')
print('buffalo will be removed from the list using remove() method,')
print(pets)

#	Using sort() method

pets.sort()
print('pets will be sorted using sort() method,')
print(pets)

pets.sort(reverse = True)
print('pets will be sorted in reverse using sort() method,')
print(pets)
