# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.

# Try either this one or next one
def print_full_name(first, last):
    line="Hello {first_name} {last_name}! You just delved into python.".format(first_name=first_name,last_name=last_name)
    return line
first_name = input()
last_name = input()
print_full_name(first_name, last_name)

# or
def print_full_name(first, last):
    print("Hello {first_name} {last_name}! You just delved into python.".format(first_name=first_name,last_name=last_name))
first_name = input()
last_name = input()
print_full_name(first_name, last_name)
