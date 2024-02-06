x = input()
count = 0
for i in range(0, len(x)):
    if(x[i] == 'H' or x[i] == 'Q' or x[i] == '9' or x[i] == '+'):
        count += 1
        break

if(count != 0):
    print("YES")
else:
    print("NO")
