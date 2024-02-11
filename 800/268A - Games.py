n = int(input())
c = 0
home = []
away = []

for i in range(0, n):
    x = input().split()
    h = int(x[0])
    a = int(x[1])
    home.append(h)
    away.append(a)

for i in range(0, n):
    for j in range(0, n):
        if(home[i] == away[j]):
            c += 1

print(c)