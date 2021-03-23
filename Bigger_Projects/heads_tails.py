"""
This is the code of a game called Coin Flip
"""

from random import randint
from time import sleep 

def get_user_guess():
    print "Menu:"
    print "0 - Heads"
    print "1 - Tails"
    guess = raw_input("Heads or tails? ")
    if guess == "0" or guess == "1":
        return int(guess)
    print "Wrong input, try again"
    get_user_guess()
    

def flip_coin():
    flip = randint(0 , 1)
    return flip

def main():
    guess = get_user_guess()
    flip = flip_coin()
    print "Fliping..."
    sleep(2)
    print "The side is: %d" % flip
        
    if guess == flip:
        print "Congratulations, you won!"
            
    else:
        print "Sorry you have lost."
            
main()
