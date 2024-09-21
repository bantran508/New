#1. Write a program that asks your name and then greets you by your name: Examples:

#If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
#If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.
#a = input("Enter your name: ")
#print("hello, "+a+"!")
#2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
#a =float(input("enter the radius: "))
#print(f"area of the circle is {3.14*a**2}")
#3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter
#and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
#a =float(input("length: "))
#b =float(input("width: "))
#print(f"perimeter of the rectangle is: {a * 2 + b * 2}")
#print(f"the area of the rectangle is: {a * b}")
#4. Write a program that asks the user for three integer numbers.
#The program prints out the sum, product, and average of the numbers.
#x, y, z = map(int, input("Enter three numbers: ").split())
#print(f"sum = {x+y+z}\nproduct = {x*y*z}\naverage = {(x+y+z)/3}")
"""5 .Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula),
and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams."""
"""
x, y, z = map(float, input("Enter the three medieval units(talents, pounds and lots): ").split())
print(f"{(x*20*32*13.3+y*32*13.3+z*13.3)//1000} kilograms and {(x*20*32*13.3+y*32*13.3+z*13.3)%1000} grams")"""
"""6.  Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6."""





