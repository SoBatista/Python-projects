#!/usr/bin/env python3

"""
This program requests to the user to enter two numbers ('x' and 'y'), and which writes the value of (x + 3 * y) / (x - y)
"""

print("Please enter two numbers: ")

x=int(input("Enter the first number, x: "))
y=int(input("Enter the second number, y: "))
print("The value of (x + 3 * y) / (x - y) is:" , (x + 3 * y) / (x - y))
