#!/usr/bin/env python3

"""
This program requests to the user to enter a number and it will return that number in days
"""

def hours_days():
   arg = float(input("Enter a number of hours and the program will convert to how many days that number of hours corresponds to: "))
   
   print(arg / 24)
    
hours_days()
