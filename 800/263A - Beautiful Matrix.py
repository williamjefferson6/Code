inputX = ""
for _ in range(5):
    row = input().strip()
    inputX += row + "\n"

rows = inputX.strip().split('\n')
x = [list(map(int, row.split())) for row in rows]
initialx = 0
initialy = 0
finalx = 2
finaly = 2

for i in range(0, 5):
    for j in range(0, 5):
        if(x[i][j] == 1):
            initialx = i
            initialy = j

diffx = abs(initialx - finalx)
diffy = abs(initialy - finaly)

print(diffx+diffy)