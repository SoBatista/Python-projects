#!/usr/bin/env python3


"""
This program requests to the user to insert a certain number of seconds and it will return the days, hours, minuts and seconds that correspond to that number
"""

sec=int(input("Enter a number of seconds that you want to transform in hours: "))
secu=(sec * 1) / 60
minu=(secu * 1) / 60
hrs=(minu * 1) / 24
print("The number of days is" , hrs)
