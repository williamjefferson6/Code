x = input().split()
n = int(x[0])
m = int(x[1])
c = 0

for i in range(0, n):
    if i % 2 == 0:
        for j in range(0, m):
            print("#",end="")
    else:
        if(c % 2 == 0):
            for j in range(0, m-1):
                print(".",end="")
            for j in range(0, 1):
                print("#", end="")
            c += 1
        else:
            for j in range(0, 1):
                print("#", end="")
            for j in range(0, m-1):
                print(".",end="")
            c += 1
    print()