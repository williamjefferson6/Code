n = int(input())
x = input().split()
x = [int(item) for item in x]
best = x[0]
worst = x[0]
count = 0

for i in range(1, n):
    if(x[i] > best):
        count += 1
        best = x[i]
    elif(x[i] < worst):
        count += 1
        worst = x[i]

print(count)