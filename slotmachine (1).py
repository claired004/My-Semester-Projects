#Claire Deng
#1/29/2025
#Slot Machine
#init
import random
import time
print("Welcome to the SLOT MACHINE. Please spin to START")

#functions
credit=100
symbols = [ "♥", "♠",  "7"]
def slotmachine():
    while True:
        spin = input("Type 'S' to Spin or 'Q' to Quit")
        if spin=="Q":
            print("Thank you for playing!")
            break
        if spin=="S":
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            print("Spinning...")
            time.sleep(2)
            print("Slots: "+slot1 +slot2 +slot3)
            random.choices(symbols,weights = [1,10,1], k=4)
            if slot1=="7" and slot2=="7" and slot3=="7":
                print("JACKPOT")
                global credit
                credit = credit*7 #x7 reward
                print("Your credit score: "+str(credit))
            elif slot1=="♥" and slot2=="♥" and slot3=="♥":
                print("Congratulations! You WON!")
                credit=credit*3 #x3 Reward
                print("Earned x4 credits\nYour credit score: " +str(credit))
            elif slot1=="♠" and slot2=="♠" and slot3=="♠":
                print("Congratulations! You WON!")
                credit=credit*3 #x3 Reward
                print("Earned x4 credits\nYour credit score: " +str(credit))
            elif slot1 ==  slot2 or slot2 == slot3:
                print("COngrat! You Won Two in a Row!")
                credit =  credit*2 #x2 reward
                print("Earned 2x credits\nour credit score: "+str(credit))
            else:
                print("LOST. No Match!")
                credit = credit-5
                print("Lost -1 credit\nYour credit score: "+str(credit))
            if credit == 0:
                print("Please get more credits to continue playing")

    #probabiliy
    #7 should be harder to hit than the other symbols
    #1. Duplicate all the symbols in your list except for 7
    #2.random.choices()probability

    #platers specifes bet
    #Winnings should be multipliers instead of set amounts
    #Do not allow player to bet more than their current balance




#1.Introduction
#2. Ask the player to spin or quit
#3.Randomly pull 3 images from our list
#advice: Remember each of these pulls(VARIABLES)
#4. Display the three images
#5. Determine the outcome(IF, ELIF, Else)

#Credit System
#Players start with 100 credits
#every spin costs 1 credit(or your choice)
#Every Jackpot results in a x100 win
#Match results in a x5 -x10
#2 of a kind x2-x5
#Loss nothing back
slotmachine()
