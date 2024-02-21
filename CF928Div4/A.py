tests = int(input())

for i in range(tests):
    s = input()
    print(max(s, key=s.count))
