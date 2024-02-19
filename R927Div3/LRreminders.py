from collections import deque

tests = int(input())
for _ in range(tests):
    lenarr, divider = map(int, input().split())
    arr = deque(map(int, input().split()))
    ans = []
    product = 1
    for command in input():
        if command == "L":
            product *= arr.popleft()
        elif command == "R":
            product *= arr.pop()
        ans.append(product % divider)
    print(*ans)
