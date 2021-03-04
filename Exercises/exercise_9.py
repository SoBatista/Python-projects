"""
This program will prompet the user to enter a number that he want move from degrees centigrade to Fahrenheit and vice versa
"""

temperature = float(raw_input("Enter a number for me to move it  from degrees centigrade to Fahrenheit and vice versa: "))

ans = raw_input("Enter a f (of Fahrenheit) or a c (of centigrade): " )

if "f" or "F":
    print temperature * 1.8 + 32, "F"

elif "c" or "C":
    print (temperature - 32) / 1.8, "C"
    
else:
    print "You did not choose a correct option!"


