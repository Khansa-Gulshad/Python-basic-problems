# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck. 

s = input().split()
print(s)
for name in s:
    r=name[0].upper()
    t=name.replace(name[0],r)
    print(t,end=" ")
    
#  or
s=input().split()
print(s)
def solve(s):
    for name in s:
        r=name[0].upper()
        t=name.replace(name[0],r)
        print(t,end=" ")
solve(s)
