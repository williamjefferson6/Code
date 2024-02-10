n = int(input())
s = input().split()
s = [int(item) for item in s]

l = [0, 0, 0, 0, 0]

for item in s:
    l[item] += 1

taxi = l[4]

taxi += l[3]
l[1] -= min(l[1], l[3])

taxi += l[2] // 2

if l[2] % 2 == 1:
    taxi += 1
    l[1] -= min(2, l[1])

taxi += l[1] // 4 + (l[1] % 4 > 0)

print(taxi)