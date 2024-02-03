str = input()
list = str.split()
n = int(list[0])
k = int(list[1])

while (k != 0):
    if(n % 10 == 0):
        n /= 10
        k -= 1
    else:
        n -= 1
        k -= 1

print(int(n))