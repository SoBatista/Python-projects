#!/usr/bin/env python3

"""
This program requests to the user to enter a sequence of numbers and in the end it will print each number in one line 
"""

number = 0
while(True):
    num=int(input("Enter a number: "))    
    if num == -1:
        print(number)
        exit()
    else:
        number = number*10+num
