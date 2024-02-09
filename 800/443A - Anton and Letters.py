x = input()
x = x[1:-1]
if x:
    x = x.split(", ")
    x = set(x)
    print(len(x))
else:
    print(0)