num=33  # secret_number
limit=5
guess = 0
print("Welcome to Number guessing Game!")
print("You have 5 attempts\nGood Luck!\n\n")
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
            print("The secret number is: ",x)
            print("You Won!!")
            break
    else:
         print("You ran out guesses!!")
         print("-----Game over-----")
         break