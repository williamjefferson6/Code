n = int(input())
l = input().split()
l = [int(item) for item in l]
max = 0
check = 1

for i in range(0, n-1):
    if(l[i] == l[i+1] or l[i] < l[i+1]):
        check += 1
    else:
        check = 1
    if(check > max):
        max = check

if(len(l) == 1):
    max = 1

print(max)