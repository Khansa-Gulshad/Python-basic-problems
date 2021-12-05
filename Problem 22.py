# You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
# The first line contains space separated integers N ,M and P.
# The next N lines contains the space separated elements of the P columns. 
# After that, the next M lines contains the space separated elements of the P columns.
# Print the concatenated array of size (N+M)XP.
# Method 1
import numpy as np
n,m,p=map(int,input().split()) # assign input values to each variables n,m,p
# map takes two inputs, one is function which is int in this case, and other is iterable object i.e. input
# the function int will iterate over all the values present in the iterable object given.
# read three no's from input and convert them into int using map() function
# n= no of rows for first array
# m=no of rows for 2nd array
# p=no of columns for both arrays
array1=np.array([input().split() for _ in range(n)],int) # _ is dummy variable it means that you are looping in the determined range but you are not going to use the index or the object during the loop
array2=np.array([input().split() for _ in range(m)],int)
print(np.concatenate((array1, array2), axis = 0)) 

# Method 2
import numpy as np
n,m,p=map(int,input().split()) 
lis=[] # create an empty list
for _ in range(n+m):
    s=input().split()
    lis.append(s) # append that list
print(np.array(lis,int))   # convert it into np.array
