"""
This program will prompete the user to insert a number of seconds and it will return to the user the correspondent number of days.

"""

sec = input("write a number of seconds: ")

mins = float((sec * 1)) / 60

hour = float((mins * 1)) / 60

days = float((hour * 1)) / 24

print("The correspondent number of days is: " , days)

"""
My calculus to get to the answer:

65432998 / 60 = 1090549.966666667min

1090549.966666667 / 60 = 18175.832777778h

18175.832777778 / 24 = 757.326365741d

"""
