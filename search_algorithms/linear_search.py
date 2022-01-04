def linear_search(sample_lst, value):
    # Time complexity = O(n)
    # Space complexity = O(1)
    for index, item in enumerate(sample_lst):
        if item == value:
            return index

    return -1


def improved_linear_search(sample_lst, value):
    # Time complexity = O(n)
    # Space complexity = O(1)
    left = 0
    length = len(sample_lst)
    right = length - 1
    for index in range(right):
        if sample_lst[left] == value:
            return left
        if sample_lst[right] == value:
            return right
        left += 1
        right -= 1

    return -1


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5]
    print(linear_search(sample1, 3))

    sample2 = [11, 20, 20, 13, 74]
    print(linear_search(sample2, 20))

    sample3 = [1, 2, 3, 4, 5]
    print(linear_search(sample3, 100))

    sample4 = [1, 2, 3, 4, 5]
    print(improved_linear_search(sample4, 3))

    sample5 = [11, 20, 20, 13, 74]
    print(improved_linear_search(sample5, 20))

    sample6 = [1, 2, 3, 4, 5]
    print(improved_linear_search(sample6, 100))
