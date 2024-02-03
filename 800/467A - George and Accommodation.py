n = int(input())
count = 0
for i in range(0, n):
    str = input()
    list = str.split()
    a = int(list[0])
    b = int(list[1])
    if (b - a >= 2):
        count += 1

print(count)