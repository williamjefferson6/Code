x = input()
y = x.upper()
check1 = False
check2 = False

if(x == y):
    check1 = True

a = x[0]
b = x[1::]
c = b.upper()

if(ord(a) > 96 and b == c):
    check2 = True

if(check1 or check2):
    p = x[0]
    q = x[1::]
    r = p.upper()
    s = q.lower()
    if(r == p):
        r = r.lower()
    print(r+s)

else:
    print(x)