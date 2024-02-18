def cut_array(input_array):
    output_array = []
    found_star = False

    for item in input_array:
        if item == "*":
            if found_star:
                break
            else:
                found_star = True
        else:
            output_array.append(item)
            found_star = False

    return output_array


def map_array(arr):
    result = []
    consecutive_stars = False

    for elem in arr:
        if elem == "@":
            result.append(1)
            consecutive_stars = False
        elif elem == ".":
            result.append(0)
            consecutive_stars = False
        elif elem == "*":
            if consecutive_stars:
                result.append(0)
            else:
                result.append(1)
            consecutive_stars = True

    return result


tests = int(input())
for _ in range(tests):
    lenarr = int(input())
    arr = list(input())[1:]
    cutted = cut_array(arr)
    print(sum(map_array(cutted)))
