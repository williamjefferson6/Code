s = input()
count = 1
check = False

for i in range(0, len(s) - 1):
    if(s[i] == s[i+1]):
        count += 1
    else:
        count = 1
    if (count == 7):
        check = True
        break

if (check == True):
    print("YES")

else:
    print("NO")