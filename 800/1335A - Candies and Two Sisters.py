t = int(input())

for i in range(0, t):
    c = 0
    n = int(input())
    if(n <= 2):
        print(c)
        continue
    else:
        if(n % 2 != 0):
            print(n // 2)
        else:
            print((n // 2)-1)