n = int(input())
l = input().split()
l = [int(item) for item in l]
r = []
for item in l:
    r.append(item)
r.reverse()
time = 0
mini = len(l) - 1 - r.index(min(l))
maxi = l.index(max(l))
time += abs(mini - (n-1))
time += abs(maxi - 0)
if(mini < maxi):
    time -= 1
print(time)