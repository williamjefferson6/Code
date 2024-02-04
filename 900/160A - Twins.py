n = int(input())
x = input().split()
x = [int(item) for item in x]
x.sort(reverse=True)
sum = sum(x)
coins = 0
temp = 0

for i in range(0, n):
    if(temp > sum):
        break
    temp += x[i]
    sum -= x[i]
    coins += 1

print(coins)