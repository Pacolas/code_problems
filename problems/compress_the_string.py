# Enter your code here. Read input from STDIN. Print output to STDOUTs
import itertools as it
s = input("")
lt  = ""
for key, group in  it.groupby(s):
    lt+=str(( len(list(group)),int(key))) + " "
print(lt)
