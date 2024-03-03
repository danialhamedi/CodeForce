import math

tests = int(input())
for _ in range(tests):
    n = int(input())
    if n == 0:
        continue
    ans = int(math.log(n, 2))
    print(2**ans)
