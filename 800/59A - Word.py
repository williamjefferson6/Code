str = input()
upp = 0
low = 0

for i in range(0, len(str)):
    if (ord(str[i]) >= 65 and ord(str[i]) <= 90):
        upp += 1
    else:
        low += 1

if(upp > low):
    print(str.upper())
else:
    print(str.lower())
