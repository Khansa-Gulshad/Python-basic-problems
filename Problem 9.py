#Nested Lists
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


my_list=[]
new_list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    data=[name,score]
    my_list.append(data)
    print(my_list)
my_list.sort(key=lambda x:x[1]) #sorting of my list x:x[1] is sorting 1 index elements i.e. scores in this case as [['khansa',12],['sadaf',23], ['hira',34]]
print(my_list)
mini=my_list[0][1] #after sorting my_list[0][1] is minimum value i.e. [0] sublist (['khansa',12]), [1] element i.e. 12
print('mini:', mini)
sec=[]
for x in my_list: #x is sublists of my_list i.e. ['khansa',12],['sadaf',23], ['hira',34]
    if (mini<x[1]): #x[1] x is sublist ['sadaf',23] while at its index 1 is 23 
        sec=x[1] # mini is less than 23 so sec=x[1]
        break #break the loop so not checking next sublists
print('sec:',sec) # it is now 23
for x in my_list:
    if sec==x[1]: #as sec==x[1] i.e. 23 so add new_list
        new_list.append(x[0]) #x[0] is 'sadaf' at sublist index 0
new_list.sort()
print('new_list:',new_list) 
for i in new_list:
    print('i:',i)
