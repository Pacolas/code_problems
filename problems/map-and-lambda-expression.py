cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    lt = []
    for i in range(n):
        if i <=0 :
            lt.append(0)
        elif i== 1:
            lt.append(1)
        else:
            lt.append(lt[i-1]+ lt[i-2])
    return lt
            
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))