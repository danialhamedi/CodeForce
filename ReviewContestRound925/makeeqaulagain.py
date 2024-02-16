import itertools as it

tests = int(input())
for _ in range(tests):
    lenghts = int(input())
    mylist = list(map(int, input().split()))
    left_weight = len(list(it.takewhile(lambda x: x == mylist[0], mylist)))
    right_weight = len(list(it.takewhile(lambda x: x == mylist[-1], mylist[::-1])))
    if mylist[0] == mylist[-1]:
        print(max(0, lenghts - (left_weight + right_weight)))
    else:
        print(lenghts - max(left_weight, right_weight))
