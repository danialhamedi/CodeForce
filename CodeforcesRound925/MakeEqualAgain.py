tests = int(input())
for _ in range(tests):
    num = int(input())
    arr = list(map(int, input().split(" ")))
    pleft = 0
    pright = num - 1
    while pleft < pright:
        leftsideinccondition = arr[pleft] == arr[pleft + 1]
        rightsideinccondition = arr[pright] == arr[pright - 1]
        if leftsideinccondition and rightsideinccondition:
            pleft += 1
            pright -= 1
        elif leftsideinccondition:
            pleft += 1
        elif rightsideinccondition:
            pright -= 1
        else:
            break
    if arr[pleft] == arr[pright]:
        if pright - pleft == 0:
            print(0)
        else:
            print(pright - pleft - 1)
    else:
        abbility = max(pleft, num - pright - 1)
        print(num - abbility - 1)
