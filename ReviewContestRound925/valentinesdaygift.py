tests = int(input())
for _ in range(tests):
    _, m = list(map(int, input().split()))
    arr = input()
    max_lenghts = len(arr.replace(" ", ""))
    if max_lenghts <= m:
        print("Anna")
    else:
        choices = sorted(
            list(map(lambda x: len(x) - len(x.rstrip("0")), arr.split())), reverse=True
        )
        order = sum([(1 if i % 2 == 0 else 0) * x for i, x in enumerate(choices)])
        if (max_lenghts - order) <= m:
            print("Anna")
        else:
            print("Sasha")
