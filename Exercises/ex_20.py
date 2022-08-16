#!/usr/bin/env python3

"""
This program calculates the number of hours an employee worked in a given week and their hourly wage and calculates the
weekly wage taking into account overtime
"""

hours=int(input("Enter the number of worked hours in a given week: "))
salary=int(input("Enter the salary per hour that you receive: "))
extra_hours=int(hours - 40)
if int(hours) <= 40:
    print("Your salary this week was" , hours * salary)
elif int(hours) > 40:
    print("Your salary this week counting overtime was" , (hours - extra_hours) * salary + (extra_hours * salary) * 2)