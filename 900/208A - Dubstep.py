x = input().split("WUB")
for item in x:
    if (item == ''):
        x.remove(item)
s = ""
for i in range(0, len(x)):
    s += x[i]
    s += " "
print(s)