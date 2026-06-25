import random
limit=5
print("Welcome to Number guessing Game!")
print("You have 5 attempts\nGood Luck!\n\n")
def progmain():
    global guess,num
    num=random.randint(1,100)  # secret_number
    guess=0      
    while True :
        if guess<limit:
            x = int(input("Enter a number: "))
            if x>num:
                print("My number is lesser than ",x)
                guess +=1
            elif x<num:
                print("My number is greater than ",x)
                guess +=1
            else:
                print("\nThe secret number is: ",x)
                print("You Won!!")
                print("-----Game over-----\n")
                break
        else:
             print("\nYou ran out guesses!!")
             print("-----Game over-----\n")
             break
while True:
    progmain()
    again=input("Do you want to play againn?? (y/n): ")
    print('\n')
    if again == 'n':
       break