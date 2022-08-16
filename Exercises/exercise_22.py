#!/usr/bin/env python3

"""
This program requests the user to enter a number of seconds and it will trensform that number in days. 
In case that the user enter a negative number the program will shutdown
"""

while(True):
    num=float(input("Enter a number of seconds: "))
    days=float((num * 1) / 86400)

    if num > 0:
        print(days)
    else:
        print("Bye!")
        exit()