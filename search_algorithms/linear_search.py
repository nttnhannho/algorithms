def linear_search(sample_lst, value):
    # Time complexity = O(n)
    # Space complexity = O(1)
    for index, item in enumerate(sample_lst):
        if item == value:
            return index
    return -1


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5]
    print(linear_search(sample1, 3))

    sample2 = [11, 20, 20, 13, 74]
    print(linear_search(sample2, 20))

    sample3 = [1, 2, 3, 4, 5]
    print(linear_search(sample3, 100))
