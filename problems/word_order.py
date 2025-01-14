# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
dicto = {}
for i in range(n):
    line = input()
    dicto[line] = dicto.get(line, 0)+1
print(len(dicto))
result  = ''
for i in dicto:
    result+=str( dicto[i] )+" "
print(result.strip())
    
