# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dicty = OrderedDict()
for i in range(n):
    line = input().split()
    name = " ".join(line[:-1])
    price  = line[-1]
    dicty[name] = dicty.get(name, 0) + int(price)
for i in dicty:
    print(i, dicty[i])
    
