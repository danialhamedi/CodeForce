num_tests = int(input())

for _ in range(num_tests):
    input()  # Discard the first input, assuming it's not used
    arr = sorted(map(int, input().split()))
    arr[0] += 1
    result = 1
    for num in arr:
        result *= num
    print(result)
