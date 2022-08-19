#!/usr/bin/env python3

"""
This program requests to the user to enter a positive integer and prints the odd digits that in that number
"""


num=int(input("Enter a positive integer: "))
resto = 0
res = 0
while num > 0:
    resto=num % 10
    if(resto%2 != 0):
        res = res *10 + resto
    num=num // 10
print(str(res)[::-1])

"""
[::-1] corresponds to start:stop:step. When you pass -1 as step, the start point goes to the end and stop at the front.
"""