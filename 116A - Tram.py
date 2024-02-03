n = int(input())
current = 0
max = 0

for i in range(0, n):
    str = input()
    list = str.split()
    exit = int(list[0])
    entry = int(list[1])
    current -= exit
    current += entry
    if(current > max):
        max = current

print(max)