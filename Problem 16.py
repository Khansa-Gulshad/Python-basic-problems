# MUTATIONS
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:
# -string string: the string to change
# -int position: the index to insert the character at
# -string character: the character to insert

def mutate_string(string, position, character):
    l=list(s)
    l[int(i)]=c
    s_new=''.join(l)
    return s_new
    
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

# or

def mutate_string(string, position, character):
    s_new=s[:int(i)] + c + s[int(i):]
    return s_new
    
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
