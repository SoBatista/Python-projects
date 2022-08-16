#!/usr/bin/env python3

"""
This program requests to the user to enter three numbers and returns the higher number 
"""

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))

if(num1 >= num2 and num1 >= num3):
    print(num1)

elif(num2 >= num1 and num2 >= num3):
    print(num2)

elif(num3 >= num1 and num3 >= num2):
    print(num3)
