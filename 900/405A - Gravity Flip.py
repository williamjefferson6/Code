n = int(input())
a = input().split()
a = [int(item) for item in a]
a.sort()
for i in range(0, n):
    print(a[i], end=" ")