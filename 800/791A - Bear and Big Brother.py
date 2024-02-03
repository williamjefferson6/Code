str = input()
list = str.split()
a = int(list[0])
b = int(list[1])
c = 0

while(a <= b):
    a *= 3
    b *= 2
    c += 1

print(c)