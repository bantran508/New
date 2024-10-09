#1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
import random
def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        result = roll_dice()
        print(f"Rolled: {result}")
        if result == 6:
            print("You rolled a 6! Stopping the rolls.")
            break

main()
#2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function
# you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling
# in the main program continues until the program gets the maximum number on the dice,
# which is asked from the user at the beginning.
import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides < 1:
                print("Please enter a positive integer for the number of sides.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        result = roll_dice(sides)
        print(f"Rolled: {result}")
        if result == sides:
            print(f"You rolled a {sides}! Stopping the rolls.")
            break
main()
#3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def gallons_to_liters(gallons):
    liters_per_gallon = 3.78541  # 1 gallon = 3.78541 liters
    return gallons * liters_per_gallon

def main():
    while True:
        try:
            gallons = float(input("Enter the volume in gallons (negative value to quit): "))
            if gallons < 0:
                print("Exiting the program.")
                break
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")
        except ValueError:
            print("Please enter a valid number.")
main()