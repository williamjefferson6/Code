str = input()
l2 = str.split()
n = int(l2[0])
t = int(l2[1])
stu = list(input())

for i in range(t):
    j = 0
    while j < n - 1:
        if (stu[j] == 'B' and stu[j + 1] == 'G'):
            stu[j], stu[j + 1] = stu[j + 1], stu[j]
            j += 2 
        else:
            j += 1

stu = ''.join(stu)
print(stu)