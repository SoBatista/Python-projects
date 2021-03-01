""" In this exercise I will prompt the user to give 2 numbers x and y and return:
(x + 3 * y) * (x - y)
"""

x = raw_input("Enter a number: ")
y = raw_input("Enter a second number: ")

res = (int(x) + 3 * int(y)) * (int(x) - int(y))

print res

