tests = int(input())
for _ in range(tests):
    scrennshots = []
    num_of_partisipants, senders = map(int, input().split())
    for _ in range(senders):
        arr = list(map(int, input().split()))
        scrennshots.append(arr[1:])
