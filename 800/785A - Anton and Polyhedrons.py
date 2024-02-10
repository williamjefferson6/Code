n = int(input())
total = 0

for i in range(0, n):
    x = input().lower()
    if(x == "tetrahedron"):
        total += 4
    elif(x == "cube"):
        total += 6
    elif(x == "octahedron"):
        total += 8
    elif(x == "dodecahedron"):
        total += 12
    else:
        total += 20

print(total)