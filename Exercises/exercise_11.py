"""
This program will prompt the user to enter a number and that it will return in days
"""

def hours_days():
   arg = float(raw_input("Enter a number of hours and the program will convert to how many days that number of hours corresponds to: "))
   
   print arg / 24
    
hours_days()
