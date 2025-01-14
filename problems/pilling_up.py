# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input( ))


for i in range(n):
    maxi = float('inf')
    response = "Yes"
    blocks = int(input())
    integers = input().split()
    rind = -1
    lind = 0
    for j in range( blocks):
        rightmost =int( integers[rind])
        leftmost = int(integers[lind])
        
        if  rightmost > maxi and rightmost > maxi :
            response = "No"
        elif rightmost > leftmost:
            rind -= 1
            maxi = rightmost
            
        else:
            lind += 1
            maxi =  leftmost
           
    print(response)
