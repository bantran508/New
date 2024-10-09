#1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints
# out the sum of the numbers. Use a for loop.
import random
num_dice = int(input("How many dice would you like to roll? "))
total = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Roll a die (1 to 6)
    total += roll  # Add the roll to the total

print(f"The total sum of the dice rolled is: {total}")
#2. Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# Initialize an empty list to store the numbers
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")
numbers.sort(reverse=True)
greatest_numbers = numbers[:5]
print("The five greatest numbers in descending order are:")
for number in greatest_numbers:
    print(number)

"""3. Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7."""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
user_input = input("Enter an integer: ")
try:
    number = int(user_input)
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
