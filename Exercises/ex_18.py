#!/usr/bin/env python3

"""
This program requests to the user to enter five real numbers and calculate the its average and standard deviation
"""

from math import sqrt
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))
num4=int(input("Enter the 4th number: "))
num5=int(input("Enter the 5th number: "))
average=(num1 + num2 + num3 + num4 + num5) / 5
c=1 / 4
print(sqrt(c * ((num1 - average) ** 2 + (num2 - average) ** 2 + (num3 - average) ** 2 + (num4 - average) ** 2 + (num5 - average) ** 2)))
