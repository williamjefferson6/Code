inp = input()
list = inp.split()
k = int(list[0])
n = int(list[1])
w = int(list[2])
total = 0

for i in range(1, w+1):
    total += i*k

if(total-n <= 0):
    print(0)

else:
    print(total-n)