x = input().split()
n = int(x[0])
k = int(x[1])

time = 4 * 60
time -= k
count = 0

for i in range(1, n+1):
    result = 5 * i
    if(time - result >= 0):
        time -= result
        count += 1
    else:
        break

print(count)