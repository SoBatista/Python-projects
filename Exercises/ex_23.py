#!/usr/bin/env python3

"""
This program requests to the user to enter a positive integer and prints the odd numbers that count in that number
"""

num=int(input("Enter a positive integer: "))
for i in num:
    if i % 2 != 0:
        print(i)
