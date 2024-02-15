n = int(input())
x = input().split()
x = [int(item) for item in x]
count = 0
check = 0

for i in range(0, n):
    if (check != 0):
        if(x[i] < 0):
            check -= 1
            continue
        else:
            check += x[i]
            continue
    elif(x[i] < 0):
        count += 1
        i += 1
    else:
        check = x[i]
        i += 1

print(count)