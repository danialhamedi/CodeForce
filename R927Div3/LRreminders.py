import math
from collections import deque

tests = int(input())
for _ in range(tests):
    lenarr, divider = map(int, input().split())
    arr = deque(map(int, input().split()))
    commands = list(input())
    ans = []
    product = math.prod(arr)
    for command in commands:
        ans.append(str(product % divider))
        if command == "L":
            product = product // arr[0]
            arr.popleft()
        elif command == "R":
            product = product // arr[-1]
            arr.pop()

    print(" ".join(ans))

# TL
