### Python If-Else
### Task
Given an integer, n , perform the following conditional actions:
1. If n is odd, print Weird
2. If n is even and in the inclusive range of to , print Not Weird
3. If n is even and in the inclusive range of to , print Weird
4. If n is even and greater than , print Not Weird

### Solution
```
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n %2==0 and 2<= n <=5:
    print('Not Weird')
elif  n %2==0 and 6<= n <=20:
    print('Weird')
elif n %2==0 and n >20:
    print('Not Weird')
```
