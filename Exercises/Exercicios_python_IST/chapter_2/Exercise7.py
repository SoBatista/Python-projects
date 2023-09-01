num = int(input("Insert a positive integer: "))
res = 0

while num > 0:
    dig = num % 10
    if dig % 2 == 0:
        res = res + dig
        
    num = num // 10
print(res)
