"""1. Write a program that asks a fisher the length of a zander in centimeters.
If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake
and notifies the user of how many centimeters below the size limit the caught fish was.
A zander must be 42 centimeters or longer to meet the size limit."""

x =float(input("the length of the zander in centimeters: "))
if x>=48:
 print("ok")
else:
 print(f"release the fish back into the lake, {42 - x} centimeters lower than the size limit")

"""2.Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written 
description according to the list below. You must use an if/elif/else structure in your solution.

LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck."""

x =str(input("enter the cabin class of a cruise ship(LUX/A/B/C): "))

if x=="LUX" :
    print("upper-deck cabin with a balcony.")
elif x=="A" :
    print("above the car deck,equipped with a window")
elif x=="B" :
    print("windowless cabin above the car deck")
else :
    print("windowless cabin below the car deck")
"""Write a program that asks for the biological gender and hemoglobin value (g/l). 
The program the notifies the user if the hemoglobin value is low, normal or high.

A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l."""
x = input("enter the biological gender : ")
y = int(input("enter the hemoglobin value (g/l) : "))
if x=="male":
    if y<117 :
        print("hemoglobin value is low")
    elif y<=134 and y>=117 :
        print("hemoglobin value is normal")
    else:
        print("hemoglobin value is high")
if x=="female":
    if y<134 :
        print("hemoglobin value is low")
    elif y>=134 and y<=167 :
        print("hemoglobin value is normal")
    else :
        print("hemoglobin value is high")

"""
4. Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only 
if they are also divisible by 400. 
"""
y = int(input("enter the year: "))
if y%4==0 :
    if y%100!=0 :
        print("leap year")
    elif y%100==0 and y%400==0 :
        print("leap year")
    else :
        print("not a leap year")
else:
    print("not a leap year")









