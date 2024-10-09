# 1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
n = 1
while n <= 1000:
    if n % 3 == 0 :
        print(n)
    n += 1
# 2.Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
n = float(input("inches: "))
m =2.54 *n
while n >= 0:
    print(f"{n} inches = {m} cm")
    break
# 3.Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
a = input("Numbers: ")

if a != "":
    smallest = largest = int(a)
    hasinput = True
else:
    hasinput = False

while a != "":
    num = int(a)
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

    a = input("Numbers: ")

if hasinput:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")




