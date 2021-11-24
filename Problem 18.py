# Input is S string.
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 

s=input()
ai=str(s)
res1=any(a.isalnum() for a in ai)    
print(res1)
res2=any(a.isalpha() for a in ai)    
print(res2)
res3=any(a.isdigit() for a in ai)    
print(res3)
res4=any(a.islower() for a in ai)   
print(res4)
res5=any(a.isupper() for a in ai)
print(res5)
