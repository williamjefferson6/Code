distance = int(input())
steps = 0

while (distance != 0):
    if (distance - 5 >= 0):
        distance -= 5
        steps += 1
    elif (distance - 4 >= 0):
        distance -= 4
        steps += 1
    elif (distance - 3 >= 0):
        distance -= 3
        steps += 1
    elif (distance - 2 >= 0):
        distance -= 2
        steps += 1
    elif (distance - 1 >= 0):
        distance -= 1
        steps += 1

print(steps)