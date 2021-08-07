import random
print("Welcome To Number Guessing Game")
print("You have to save the world by decoding the number!")
number=random.randint(1,9)
shoppingList=['eggs','milk','bread','meat']
chance=5
while(chance>0):
    playerGuess=int(input("Choose A Number From 1-9: "))
    if (playerGuess==number):
        print("You saved the world Congragulations")
        break
    elif (playerGuess<number) :
        print("Try To Guess Higher Than", playerGuess)
    else:
        print("Try To Guess Lower Than", playerGuess)
    chance=chance-1
if(chance==0):
    print("Don't worry! You can Try Again!")
    print("Make Sure To Get",shoppingList)
