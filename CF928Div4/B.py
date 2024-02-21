tests = int(input())

for i in range(tests):
    n = int(input())
    a = []
    for _ in range(n):
        thisline = [int(char) for char in input()]
        sumof = sum(thisline)
        if sumof > 0:
            a.append(sumof)
    fl = True
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            fl = False
    if fl:
        print("SQUARE")
    else:
        print("TRIANGLE")
