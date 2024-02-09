n = int(input())
c = 0
while (n != 0):
    if(n >= 100):
        x = n // 100
        c += x
        n -= (x * 100)
    elif(n >= 20):
        x = n // 20
        c += x
        n -= (x * 20)
    elif(n >= 10):
        x = n // 10
        c += x
        n -= (x * 10)
    elif(n >= 5):
        x = n // 5
        c += x
        n -= (x * 5)
    else:
        x = n // 1
        c += x
        n -= (x * 1)

print(c)