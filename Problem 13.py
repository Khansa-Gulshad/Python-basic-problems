#sWAP cASE
# Replace lower case letters with upper case and visa virsa.
def swap_case(s):
    return s.swapcase()
s = input()
result = swap_case(s)
print(result)

# or
def swap_case(string):
    result=""
    for letter in s:
        if letter==letter.lower():
            result+=letter.upper()
        else:
            result+=letter.lower()
    return result

string = input()
result = swap_case(string)
print(result)
