str = input()
str2 = input()
list = str.split()
n = int(list[0])
h = int(list[1])
x = 0
list = str2.split()

for i in range(0, n):
    if(int(list[i]) > h):
        x += 1

n -= x
total = n + (x * 2)
print(total)