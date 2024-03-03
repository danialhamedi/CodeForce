test = int(input())

for _ in range(test):
    _ = input()
    arr = list(map(int, input().split()))
    reminder = sum(arr) % 3
    if reminder == 0:
        print(0)
    elif (reminder == 1 and 1 in arr) or reminder == 2:
        print(1)
    elif (
        len(
            list(
                filter(
                    lambda x: x % 3 == 0,
                    (map(lambda x: x - reminder if x >= 3 else x, arr)),
                )
            )
        )
        >= 1
    ):
        print(1)
    else:
        print(2)
