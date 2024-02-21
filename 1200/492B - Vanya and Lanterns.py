x = input().split()
n = int(x[0])
l = int(x[1])
a = input().split()
a = [int(item) for item in a]
a.sort()
maxdist = -999

for i in range(0, n-1):
    dist = a[i+1] - a[i]
    if (dist > maxdist):
        maxdist = dist

end = a[0] - 0
start = l - a[n-1]

d = max(maxdist/2,max(end,start))

print(d)