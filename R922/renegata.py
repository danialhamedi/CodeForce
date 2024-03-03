test = int(input())

for _ in range(test):
    _ = input()
    print(sum(map(abs, list(map(int, input().split())))))
