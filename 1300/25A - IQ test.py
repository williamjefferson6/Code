n = int(input())
x = input().split()
x = [int(item) for item in x]
odd = 0
even = 0

for item in x:
    if item % 2 == 0:
        even += 1
    else:
        odd += 1

if(odd > even):
    for i in range(0, n):
        if(x[i] % 2 == 0):
            print(i+1)
else:
    for i in range(0, n):
        if(x[i] % 2 != 0):
            print(i+1)