#!/usr/bin/env python3

"""
This program requests to the user to insert the number of passagers to be carried on the plane and calculates the plane's consumption in gallons/mile
"""

passagers=int(input("Enter the number of passagers: "))
gallon=(passagers * 1) / 22
print("The plain had" , passagers , "passagers and the consumption of the plane in gallons per mile is" , gallon)

