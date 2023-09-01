#This program will prompete the user to enter a number of seconds. Then, the program will return to the user the correspondent number of days.

num = input("write a number of seconds: ")

while int(num) > 0:
    days = float((num * 1)) / 86400
    print("The correspondent number of days is: " , days)
    num = input("write a number of seconds: ")
