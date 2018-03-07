import sys

def collatz(number):
    if(number%2 == 0):
        number = number // 2
    elif(number%2 != 0):
        number = (number * 3) + 1
    else:
        print("Exception")
    return number

number = int(input("Enter an integer for collatz : "))

if(number == 0 or number < 0):
    print("Exception")
    sys.exit()

while(number != 1):
    number = collatz(number)
    print(number)
