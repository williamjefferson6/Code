n = int(input())
xi = 0
yi = 0
zi = 0

for i in range(0, n):
    inp = input()
    l = inp.split()
    xi += int(l[0])
    yi += int(l[1])
    zi += int(l[2])

if(xi == 0 and yi == 0 and zi == 0):
    print("YES")
else:
    print("NO")
