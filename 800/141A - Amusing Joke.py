a = input()
b = input()
c = input()

for item in c:
    if item in a:
        a = a.replace(item, "", 1)
    elif item in b:
        b = b.replace(item, "", 1)
    else:
        print("NO")
        break
else:
    if(len(a) != 0 or len(b) != 0):
        print("NO")
    else:
        print("YES")