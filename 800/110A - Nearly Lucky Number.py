x = int(input())
digits = 0

while (x != 0):
    if(x % 10 == 4 or x % 10 == 7):
        digits += 1
    x = x // 10

if (digits == 4 or digits == 7):
    print("YES")
else:
    print("NO")