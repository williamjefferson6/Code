n = int(input())
str = input()
list = str.split()
x = False

for i in range(0, n):
    if(int(list[i]) == 1):
        x = True

if (x == True):
    print("HARD")
else:
    print("EASY")