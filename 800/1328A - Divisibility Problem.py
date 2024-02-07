t = int(input())
l = []

for _ in range(t):
    a, b = map(int, input().split())
    result = a % b
    if result == 0:
        l.append(0)
    else:
        result = b - result
        l.append(result)

for item in l:
    print(item)