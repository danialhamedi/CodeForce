def check_conditions(pair, x, y):
    return (pair[0] + pair[1]) % x == 0 and (pair[0] - pair[1]) % y == 0


numtest = int(input())
for _ in range(numtest):
    a, x, y = map(int, input().split())
    my_list = list(map(int, input().split()))
    count = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if check_conditions((my_list[i], my_list[j]), x, y):
                count += 1
    print(count)
