'''
Python program to pass parameter to the function and get a return value, implementing the magic 8 ball example.
Author : thegothamstak
Date : 30th March 2018
'''
import random

#Function definition. Accepting a parameter through answerNumber.
#Using return statement to return a value from the function.
def getAnswer(answerNumber):
	if(answerNumber == 1):
		return 'It is certain'
	elif(answerNumber == 2):
		return 'It is decidedly so'
	elif(answerNumber == 3):
		return 'Yes'
	elif(answerNumber == 4):
		return 'Reply hazy try again'
	elif(answerNumber == 5):
		return 'Ask again later'
	elif(answerNumber == 6):
		return 'Concentrate and ask again'
	elif(answerNumber == 7):
		return 'My reply is no'
	elif(answerNumber == 8):
		return 'Outlook not so good'
	elif(answerNumber == 9):
		return 'Very doubtful'

#To get a random number between 1 - 9
r = random.randint(1,9)

#Value returned from the function will be stored in the fortune variable.
fortune = getAnswer(r)

#Printing fortune
print(fortune)