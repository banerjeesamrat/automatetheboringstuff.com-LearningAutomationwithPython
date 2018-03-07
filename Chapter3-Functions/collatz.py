user = 0

def collatz(number):
    if(number%2==0):
        return(number//2)
        
    elif(number%2!=0):
        return((3*number)+1)

try:
    user=int(input('Enter an integer\n'))
    if(user<=0):
        print("Only positive integers")
    else:
        while(True):
            user=collatz(user)
            print(user)

            if(user==1):
                break

except ValueError:
    print('Enter an integer only')


    


    
        

