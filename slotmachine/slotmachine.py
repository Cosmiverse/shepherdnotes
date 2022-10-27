from operator import truediv
import random
from tokenize import Number

def checkNumber(num, debug):
    try:
        num = float(num)
    except:
        if debug:
            print("Input must be a number.")
        return False
    if num > 0:
            return True
    else:
        if debug:
            print("Input must be larger than 0.")
        return False

def main():
    print("Welcome to the Shepherd Slot Machine!")
    money = 0
    bet = 0
    while not checkNumber(money, False):
        money = input("Please enter the amount of money to begin with: $")
        num = checkNumber(money, True)
    while not checkNumber(bet, False):
        bet = input("Please enter the amount of money to bet: $")
        num = checkNumber(bet, True)

main()