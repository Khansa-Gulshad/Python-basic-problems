### Find the Runner-Up Score!
### Task 
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given `n` scores. Store them in a list and find the score of the runner-up. 
### Solution 
```ruby
n = int(input())
arr = map(int, input().split())
arr=list(arr)
m=max(arr)
while max(arr)==m:
    arr.remove(max(arr))
print(max(arr))
```
or 
```ruby
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr))[-2])
```
