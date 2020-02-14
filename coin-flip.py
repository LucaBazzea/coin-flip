import random
from IPython.display import clear_output

option1 = " "
option2 = " "
assign = " "

def values():

    while assign == " ":
        assign = input("Would you like to assign values to the coin? y:Yes n:No").lower()

        if assign == "y":
            


def coin_flip():

    clear_output()
        flip = random.randint(0,1)

    if flip == 0:
            print(f"Heads {option1}")
        else:
            print(f"Tails {option2}")

coin_flip()