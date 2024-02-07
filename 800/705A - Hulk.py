x = int(input())

for i in range(1, x+1):
    if(i % 2 != 0):
        print("I hate", end=" ")
    else:
        print("I love", end=" ")
    if(i == x):
        print("it")
    else:
        print("that", end=" ")