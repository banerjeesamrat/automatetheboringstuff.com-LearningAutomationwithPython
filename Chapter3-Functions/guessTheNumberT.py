'''
    Python program to guess the number within 6 attempts.
    Author : thegothamstak
    Date : 30th March 2018
'''
import random

#Flag is set to Y to start with the first attempt in while loop
goAgain = 'Y'

#while loop introduced so that player can play the guessing game again without having to run the whole program again
while(goAgain == 'Y'):
    #Generates a random number in range 1 - 20
    secretNumber = random.randint(1,20)
    print('I am thinking of a number between 1 and 20')

    #6 attempts at guessing
    for guessTaken in range(1,7):
        guess = int(input("Take a guess : "))

        if(guess < secretNumber):
            print('Your guess is too low')
        elif(guess > secretNumber):
            print('Your guess is too high')
        else:
            break

    #Checks whether correct number was guessed or the player ran out of attempts
    if(guess == secretNumber):
        print('Nice job ! You guessed the number in '+str(guessTaken)+' guesses !')
    else:
        print('Well played ! But the number I was thinking of was '+str(secretNumber))

    #If the player wants to take a chance at it again
    goAgain = input('Do you want to go again ? (For Yes enter [Y]) : ')
