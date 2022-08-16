#!/usr/bin/env python3

"""
This program requests to the user to enter a number that he want to move from degrees centigrade to Fahrenheit and vice versa
"""

temperature = float(input("Enter a number for me to move it  from degrees centigrade to Fahrenheit and vice versa: "))

ans = input("Enter a f (of Fahrenheit) or a c (of centigrade): " )

if "f" or "F":
    print(temperature * 1.8 + 32, "F")

elif "c" or "C":
    print((temperature - 32) / 1.8, "C")
    
else:
    print("You did not choose a correct option!")


