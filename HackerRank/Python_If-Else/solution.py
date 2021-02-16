"""Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0

n = 3
n is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1

n = 24
n > 20 and n  is even, so it is not weird."""
 
# solution

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    
    if type(n) == int and 1 <= n <= 100:

        if n % 2 == 1:
            print "Weird"
        
        #If n is even and in the inclusive range of 2 to 5, print Not Weird
        
        if n % 2 == 0 and 2 <= n < 5:
            print "Not Weird"
        
        #If n is even and in the inclusive range of 6 to 20, print Weird
        
        if n % 2 == 0 and 6 <= n <= 20:
            print "Weird"
            
        #If n is even and greater than 20, print Not Weird
        
        if n % 2 == 0 and n > 20:
            print "Not Weird"
    
    
