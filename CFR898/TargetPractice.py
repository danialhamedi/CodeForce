num_tests = int(input())

for _ in range(num_tests):
    target = [list(input()) for _ in range(10)]
    res = 0
    for r, row in enumerate(target):
        for c, value in enumerate(row):
            if value == 'X':
                if r in {9, 0} or c in {9, 0}:
                    res += 1
                elif r in {1, 8} or c in {1, 8}:
                    res += 2
                elif r in {2, 7} or c in {2, 7}:
                    res += 3
                elif r in {3, 6} or c in {3, 6}:
                    res += 4
                elif r in {4, 5} or c in {4, 5}:
                    res += 5
    print(res)
