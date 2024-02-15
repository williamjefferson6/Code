n = int(input())
name_counter = {}
response_list = []

for i in range(n):
    name = input()
    count = name_counter.get(name, 0)
    if count == 0:
        response_list.append("OK")
    else:
        new_name = name + str(count)
        response_list.append(new_name)

    name_counter[name] = count + 1

for response in response_list:
    print(response)