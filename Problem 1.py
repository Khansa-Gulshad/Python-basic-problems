# Python If-Else
# Task
# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of to , print Not Weird
# If n is even and in the inclusive range of to , print Weird
# If n is even and greater than , print Not Weird

# Solution
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n %2==0 and 2<= n <=5:
    print('Not Weird')
elif  n %2==0 and 6<= n <=20:
    print('Weird')
elif n %2==0 and n >20:
    print('Not Weird')

    
