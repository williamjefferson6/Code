n = int(input())
s = input()
s = s.lower()

unique = set()
for char in s:
    if char.isalpha():
        unique.add(char)

if(len(unique) == 26):
    print("YES")
else:
    print("NO")