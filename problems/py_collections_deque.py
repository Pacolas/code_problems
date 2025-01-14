from collections import deque

n = int(input())
d = deque()
for i in range(n):
    line = input().split()
    ins = line[0]
    if len(line) >1:
        num  = line[1]
        eval(f"d.{ins}('{num}')")
    else:
        eval(f"d.{ins}()")
result = ""
for i in d:
    result+= i +" "
print(result.strip())
        
