#Write a Function
#Task
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet 
# takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# 1. The year can be evenly divided by 4, is a leap year, unless:
# 2. The year can be evenly divided by 100, it is NOT a leap year, unless:
# 3. The year is also evenly divisible by 400. Then it is a leap year.

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    if year %400 == 0:
        return True
    if year %100==0:
        return False
    if year %4==0:
        return True
    else:
        return False

year = int(input())
is_leap(year)

# or another way


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

#or by this method
 def is_leap(year):
    leap = False
    if year%4==0 and year%100 !=0:
        return True
    elif year%100 ==0 and year%400 !=0:
        return False
    elif year%400 ==0:
        return True
    return leap

