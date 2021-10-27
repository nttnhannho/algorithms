def recursive_binary_search_sorted(sample_lst, left, right, value):
    # Time complexity = O(log(n))
    # Space complexity = O(log(n))
    if left < right:
        mid = left + (right - left) // 2
        mid_val = sample_lst[mid]
        if mid_val == value:
            return mid
        if value < mid_val:
            return recursive_binary_search_sorted(sample_lst, left, mid - 1, value)
        if value > mid_val:
            return recursive_binary_search_sorted(sample_lst, mid + 1, right, value)
    return -1


def iterative_binary_search_sorted(sample_lst, value):
    # Time complexity = O(log(n))
    # Space complexity = O(1)
    left = 0
    right = len(sample_lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = sample_lst[mid]
        if mid_val == value:
            return mid
        elif value < mid_val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5]
    print(recursive_binary_search_sorted(sample1, 0, len(sample1) - 1, 3))

    # sample2 = [11, 20, 20, 130, 74]  # return 2 because 20 is at middle index
    # print(recursive_binary_search_sorted(sample2, 0, len(sample2) - 1, 20))

    sample3 = [1, 2, 3, 4, 5]
    print(recursive_binary_search_sorted(sample3, 0, len(sample3) - 1, 100))

    sample4 = [1, 2, 3, 4, 5]
    print(iterative_binary_search_sorted(sample4, 3))

    # sample5 = [11, 20, 20, 130, 74]  # return 2 because 20 is at middle index
    # print(iterative_binary_search_sorted(sample5, 20))

    sample6 = [1, 2, 3, 4, 5]
    print(iterative_binary_search_sorted(sample6, 100))
