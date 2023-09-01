# This program will prompet the user to incert numbers. Then the program will end if the user incert the number -1 and it will print all the numbers incerted (by the user) in the given order. 

num = int(input("write the number you want to introduce: "))
res = 0

while num != -1:
    res = res * 10 + int(num)
    num = int(input("write the number you want to introduce (Write -1 if you want to exit: ): "))

print(res)
 
 
"""
example: 

1
res = 0 *10 + 1 = 1
2
res = 1 * 10 + 2 = 12
3
res = 12 * 10 + 3 = 123
5
res = 123 * 10 + 5 = 1235 
-1
result: 1235
"""
