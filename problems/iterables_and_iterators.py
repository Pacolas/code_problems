import itertools as it

n = int(input())
s = input().replace(" ","")
t = int(input())
x = (list(it.combinations(s[:n],t)))
total = 0
for i in x:
    if i.count("a")>0:
        total += 1
resp =round( (total/len(x)),3)
print(resp)
