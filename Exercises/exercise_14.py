#!/usr/bin/env python3

"""
This program requests to the user to enter two numbers corresponding to a distance traveled (in km) and the time required to cover it (in minutes), and calculates the average speed in: 
(a) Km / h 
(b) m / s
"""

print("Please enter the vales to calculate the average speed traveled: ")

km=float(input("Enter the Kilometers done by you: "))
minutes=float(input("Enter the time in minuts that you did while doing the Kilometers: "))
hours=(minutes * 1) / 60
meters=(km * 1000)
seconds=(minutes * 60)
print("You did" , (km / hours))
print("You did" , (meters / seconds))

