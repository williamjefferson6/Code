def distinct_year(year):
    year = str(year)
    year = set(year)
    if len(year) == 4:
        return True
    else:
        return False

year = int(input()) + 1
while True:
    if distinct_year(year):
        print(year)
        break
    else:
        year += 1
