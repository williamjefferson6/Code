n = int(input())
s = input()
l = s.split()
l2 = []

for i in range(0, n):
    l2.append('0')

for i in range(0, n):
    l2[int(l[i]) - 1] = i + 1

l2 = " ".join(map(str, l2))
print(l2)