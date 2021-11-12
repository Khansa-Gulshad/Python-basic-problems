# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    count=0
    sub_len=len(sub_string)
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+sub_len] == sub_string:
            count+=1
    return count

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)

# or 
def count_substring(string, sub_string):
    count=0
    lens=len(string)-len(sub_string)+1
    sub_len=len(sub_string)
    for i in range(lens):
        if string[i:i+sub_len] == sub_string:
            count+=1
    return count

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)
