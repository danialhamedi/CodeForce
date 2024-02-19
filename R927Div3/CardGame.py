for _ in range(int(input())):
    n = int(input())
    t = input()
    a = list(input().split())
    a = sorted(a, key=lambda x: (x[1] == t, x[1], x[0]))
    print(a)
