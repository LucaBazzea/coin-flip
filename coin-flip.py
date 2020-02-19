import random
import time

def value_assign():

        assign = " "

        while assign != "y" and assign != "n":
                assign = input("Would you like to assign values to the coin? [y,n]: ").lower()
    
        option1 = " "
        option2 = " "
    
        if assign == "y":
            while option1 == " ":
                option1 = input("Heads: ")
            while option2 == " ":
                option2 = input("Tails: ")
        return option1, option2


def coin_flip():

        option1, option2 = value_assign()
        flip = random.randint(0,1)

        print("---Flipping Coin---")

        time.sleep(2.5)

        if flip == 0:
            print(f"Heads {option1}")
        else:
            print(f"Tails {option2}")

coin_flip()


# input = ("would you like to flip again? [y:n]")
# would you like to start a new coin [y:n]
# 