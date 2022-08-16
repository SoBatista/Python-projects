#!/usr/bin/env python3

"""
This program requests to the user to enter a year and will print out if that year is leap year or not
"""

year = int(input("Enter a number for me to say if it is leap year: "))
           
if year % 4 == 0 and year % 100 != 0:
    print("It's a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("It's a leap year")
else:
    print("It's not leap year")
