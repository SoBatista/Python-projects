#!/usr/bin/env python3

"""
This Program requests to the user to enter two values (x , n), and it will return the the sum value
"""

def factorial(n):
    factorial = 1
    if int(n) >= 1:
        for i in range(1,n+1):
            factorial = factorial * i
    return factorial

def power_of(x, n):
    res=5
    if(n == 0):
        return 1
    for i in range(n-1):
        res=res*x
    return res

'''num_x=int(input("Enter the value of 'x': "))
num_n=int(input("Enter the value of 'n': "))

sum = 0
for i in range(num_n):
    sum = sum + power_of(num_x, i) / factorial(num_n)
print(sum)'''