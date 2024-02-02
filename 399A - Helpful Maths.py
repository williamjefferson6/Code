s = input()
length = len(s)
list = []
for i in range (0, length):
    if (i % 2 == 0):
        list.append(int(s[i]))

result = ''
list.sort()
j = 0
for i in range(0, length):
    if (i % 2 == 0):
        result += str(list[j])
        j+=1
    else:
        result += s[i]
print(result)