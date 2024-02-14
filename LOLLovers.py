def divide_food(n, items):
    valid_divisions = (
        i for i in range(1, n) if items[:i].count("L") != n - 2 * items[:i].count("L")
    )
    return next(valid_divisions, -1)


n = int(input())
items = input().strip()
print(divide_food(n, items))
