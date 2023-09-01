#This program will prompete the user to enter three numbers. Then, the program will printe the gratest one.

print("Write three numbers in the order that the machine asks you to: ")

num1 = int(input("1º number: "))
num2 = int(input("2º number: "))
num3 = int(input("3º number: "))

if num1 > num2 and num1 > num3:
    print("The greatest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)
