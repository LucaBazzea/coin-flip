import random
from IPython.display import clear_output


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
        else:
                print("No")

value_assign()

def coin_flip():

    clear_output()
    flip = random.randint(0,1)

    if flip == 0:
            print(f"Heads {option1}")
    else:
            print(f"Tails {option2}")

coin_flip()