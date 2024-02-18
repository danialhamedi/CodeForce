tests = int(input())
for _ in range(tests):
    lenarr = int(input())
    arr = list(map(int, input().split()))
    current_year = arr[0]
    arr = arr[1:]
    for elem in arr:
        subtract = elem - current_year
        modulo = subtract % elem
        if modulo == 0:
            current_year += elem
        else:
            current_year = current_year + modulo
    print(current_year)
