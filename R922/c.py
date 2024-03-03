def solution(arr):
    while len(arr) > 1:
        if arr[0] == arr[1]:
            F = next(
                (index for index, value in enumerate(arr) if value != arr[0]), None
            )
            if F is not None:
                arr[1], arr[F] = arr[F], arr[1]
                sel = arr[0] % arr[1]
                arr[1] = sel if sel != arr[0] else arr[1] - sel
                arr = arr[1:]
            else:
                print("No")
                return
        else:
            arr[1] = arr[0] % arr[1]
            arr = arr[1:]
    if arr[0]:
        print("YES")
    else:
        print("NO")


test = int(input())
for i in range(test):
    _ = int(input())
    arr = list(map(int, input().split()))
    solution(arr)
