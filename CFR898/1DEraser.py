num_of_test = int(input())

for _ in range(num_of_test):
    n, k = map(int, input().split())
    string = input()
    res = string.count('B', 0, n)
    res += (res // k) * (k - 1)
    print(res)