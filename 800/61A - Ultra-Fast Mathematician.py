x = input()
y = input()
s = ""

for i in range(0, len(x)):
    if(x[i] == y[i]):
        s += "0"
    else:
        s += "1"

print(s)