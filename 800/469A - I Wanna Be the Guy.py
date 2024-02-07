n = int(input())
x = input().split()
y = input().split()
x.pop(0)
y.pop(0)
x = [int(item) for item in x]
y = [int(item) for item in y]
l = []

for i in range(1, n+1):
    check = False
    if i in x:
        check = True
    if i in y:
        check = True
    if(check == True):
        l.append(1)
        check = False

if(len(l) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")