#!/usr/bin/env python3

"""
This program is a basic calculator
"""

def mul(arg1, arg2):
    return arg1*arg2

def add(arg1, arg2):
    return arg1 + arg2


def div(arg1, arg2):
    return arg1 / arg2

def sub(arg1, arg2):
    return arg1 - arg2

def squa(arg1):
    return arg1 ** 2


def main():
    print("Wellcome!")
    while(True):
        print("Menu:")
        print("1 - Multiplication")
        print("2 - Addition")
        print("3 - Division")
        print("4 - Subtraction")
        print("5 - Squared")
        print("0 - Exit")
        
        option =  input("Enter a number from the menu: ")
        if option == "0":
            print("Bye!")
            return "Exit"
        elif option == "1":
            arg1 = input("Enter the first number: ")
            arg2 = input("Enter the second number: ")
            res = mul(int(arg1), int(arg2))
            print(res)
        elif option == "2":
            arg1 = input("Enter the first number: ")
            arg2 = input("Enter the second number: ")
            res = add(int(arg1), int(arg2))
            print(res)
        elif option == "3":
            arg1 = input("Enter the first number: ")
            arg2 = input("Enter the second number: ")
            res = div(int(arg1), int(arg2))
            print(res)
        elif option == "4":
            arg1 = input("Enter the first number: ")
            arg2 = input("Enter the second number: ")
            res = sub(int(arg1), int(arg2))
            print(res)
        elif option == "5":
            arg1 = input("Enter the number: ")
            res = squa(int(arg1))
            print(res)
        
main()        
