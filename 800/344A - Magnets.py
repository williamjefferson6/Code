magnet = 1
inp = int(input())
last = int(input())

for i in range(0, inp-1):
    x = int(input())
    if (last != x):
        magnet += 1
        last = x

print(magnet)