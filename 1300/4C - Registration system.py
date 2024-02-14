n = int(input())
l = []
for i in range(0, n):
    s = input()
    check = 0
    l.append(s)
    for item in l:
        if(item == s):
            check += 1
    if(check == 1):
        print("OK")
    else:
        print(s+str(check-1))
    check = 0