check = "hello"
s = input()
j = 0

for i in range(0, len(s)):
    if (j > 4):
        break
    if (s[i] == check[j]):
        j += 1

if (j > 4):
    print("YES")
else:
    print("NO")