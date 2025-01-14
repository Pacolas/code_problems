if __name__ == '__main__':
    N = int(input())
    lt= [ ]
    for i in range(N):
        line =  input().split()
        inst  = line[0]
        params = len(line) -1
        if inst == "print":
            print(lt)
        elif params == 1:
            eval(f"lt.{inst}({line[1]})")
        elif params == 2:
            eval(f"lt.{inst}({line[1]}, {line[2]})")
        else:
            eval(f"lt.{inst}()")