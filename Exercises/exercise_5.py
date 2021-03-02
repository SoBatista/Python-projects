"""
In this program, I will prompt the user to enter a number and print out if that number is negative, positive or zero 
"""

number = raw_input("Enter a number for me to say if it is negative, positive or zero: ")

if int(number) < 0:
    print "Negative"
        
elif int(number) == 0:
    print "Zero"
    
else:
    print "Positive"

