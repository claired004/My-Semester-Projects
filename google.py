#Claire Deng

#init
import random
def game():
    print("Welcome to the Number Guessing Game!")
    print("Guess the random number the computer generates. You have 3 guesses to see beat the computer!")
    guess = int(input("Enter Guess 1:")) #integer
    secret = random.randint(0,10) #integer
    two = int(input("Enter Guess 2: "))
    three = int(input("Enter Guess 3: "))
    if guess == secret:
        print("correct")
    if two == secret:
        print("Guess 1 is correct!")
    if three == secret:
        print("Guess 3 is correct!")
    elif three!= secret and two !=secret and guess!=secret:
            print("no right gueses the correct answer was" +str(secret)+", thanks for playing!")


#function

#main
game()

