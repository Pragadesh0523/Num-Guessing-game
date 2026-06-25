num=33
while True :
    x = int(input("Enter a Number: "))
    if x>num:
        print("My number is lesser than ",x)
    elif x<num:
        print("My number is greater than ",x)
    else:
        print("The secret number is: ",x)
        print("You Won!!")
        break
