from math import factorial

x = int(input("What's the value of x? "))
n = int(input("what's the value of n? "))

sum = 0
i = 0

while i <= n:
    res = (x**i) / factorial(i)
    sum = sum + res
    i = i + 1


print("the value of the sum is " , sum)