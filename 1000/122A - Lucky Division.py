def is_lucky_number(n):
    digits = 0
    y = n
    while(n != 0):
        if(n % 10 == 4 or n % 10 == 7):
            digits += 1
        n = n // 10
    if(digits == len(str(y))):
        return True
    else:
        return False

x = int(input())
check = False
for i in range(0, x+1):
    if(is_lucky_number(i) and (x % i == 0)):
        check = True
        break

if(check == True):
    print("YES")
else:
    print("NO")