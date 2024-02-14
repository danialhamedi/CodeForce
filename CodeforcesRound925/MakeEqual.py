tests = int(input())
for _ in range(tests):
    numofcontainers = int(input())
    containers = list(map(int, input().split(" ")))
    totalwater = sum(containers)
    desiredstate = totalwater / numofcontainers
    extra = 0
    possible = True
    for i, value in enumerate(containers):
        if value > desiredstate:
            extra += value - desiredstate
        elif value < desiredstate:
            if extra >= desiredstate - value:
                extra -= desiredstate - value
            else:
                possible = False
                break
    if possible:
        print("YES")
    else:
        print("NO")
