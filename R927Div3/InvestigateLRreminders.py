import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()

    idx = []
    left = 0
    right = n - 1

    for i in range(n):
        if s[i] == "L":
            idx.append(left)
            left += 1
        else:
            idx.append(right)
            right -= 1

    print(idx)

    ans = []
    tmp = 1
    for i in range(n):
        tmp *= a[idx[n - 1 - i]]
        tmp %= m
        ans.append(tmp)

    print(*ans[::-1])
