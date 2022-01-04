import math


def jump_search(sample_lst, value):
    # Time complexity = O(sqrt(n))
    # Space complexity = O(1)
    length = len(sample_lst)
    step = int(math.sqrt(length))

    prev = 0
    while sample_lst[min(step, length) - 1] < value:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1

    for index, item in enumerate(sample_lst[prev:step], start=prev):
        if item == value:
            return index


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5, 6, 7]
    for i in range(1, len(sample1) + 1):
        print(jump_search(sample1, i))

    sample2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(jump_search(sample2, 100))
