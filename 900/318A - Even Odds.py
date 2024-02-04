x = input().split()
n = int(x[0])
k = int(x[1])

mid = (n + 1) // 2

if k <= mid:
    val = 1 + (k - 1) * 2
else:
    val = 2 + (k - mid - 1) * 2

print(val)
