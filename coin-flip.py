import random
import time
import os

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

def end_menu():
    
    menu = " "

    time.sleep(1)

    while menu != "1" and menu != "3":
        print(" ")
        print("Would you like to...")
        menu = input("[1] Flip again [3] Close the app: ")

    if menu == "1":
        coin_flip()
    else:
        print(" ")
        time.sleep(1)
        print("Good Bye")
        quit()

def coin_flip():

    option1, option2 = value_assign()

    flip = random.randint(0,1)

    print("---Flipping Coin---")
    time.sleep(0.75)
    print(" ")
    time.sleep(0.75)
    print(" ")
    time.sleep(0.75)

    if flip == 0:
        print(f"Heads {option1}")
    else:
        print(f"Tails {option2}")

    end_menu()
    
coin_flip()