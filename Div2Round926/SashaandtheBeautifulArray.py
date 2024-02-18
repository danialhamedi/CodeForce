tests = int(input())
for _ in range(tests):
    lenarr = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = sum([(arr[x + 1] - arr[x]) for x in range(0, lenarr - 1)])
    print(ans)
