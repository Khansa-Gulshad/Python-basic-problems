# Print the average of the marks array for the student name provided, showing 2 places after the decimal. 
#example input 'harry': [50,60,40]
# average of marks with 2 decimal places

# Solution
from statistics import mean
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    avg_dic={}
    for k,v in student_marks.items():
        avg_dic[k]=mean(v)
query_name = input()
print("%.2f" % avg_dic[query_name]) 

#this last step is simply explained as:
#d = str(input("Enter what you want: "))
# p  = {'a': '1', 'b': '2', 'c':'3'}
# print(p[d])
