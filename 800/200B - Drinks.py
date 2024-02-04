n = int(input())
x = input().split()
x = [int(item) for item in x]
percent = 0

for i in range(0, n):
    percent += x[i]

percent = percent / (n * 100)
print(percent*100)