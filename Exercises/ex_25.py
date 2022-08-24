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
    res=x
    if(n == 0):
        return 1
    for i in range(n-1):
        res=res*x
    return res

def runMain(num_x, num_n):
    sum = 0
    for i in range(num_n+1):
        val1 = power_of(num_x, i)
        val2 = factorial(i)
        sum = sum + (val1 / val2)
    return format(sum, ".2f")

if __name__ == '__main__':
    num_x=int(input("Enter the value of 'x': "))
    num_n=int(input("Enter the value of 'n': "))
    print(runMain(num_x, num_n))