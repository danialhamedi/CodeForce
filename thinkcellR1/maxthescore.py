tests = int(input())

for i in range(tests):
    numofnumbers = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    ans = sum([min(arr[i], arr[i + 1]) for i in range(0, 2 * numofnumbers - 1, 2)])
    print(ans)
