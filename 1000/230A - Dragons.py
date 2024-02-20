s, n = map(int, input().split())

dragons = []
for i in range(0, n):
    x, y = map(int, input().split())
    dragons.append((x, y))

dragons.sort()

for dragon in dragons:
    if s <= dragon[0]:
        print("NO")
        break
    else:
        s += dragon[1]
else:
    print("YES")