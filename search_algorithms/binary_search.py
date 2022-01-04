def recursive_binary_search_sorted(sample_lst, left, right, value):
    # Time complexity = O(log(n))
    # Space complexity = O(log(n))
    if left > right:
        return -1

    mid = (left + right) // 2
    mid_val = sample_lst[mid]
    if mid_val == value:
        return mid
    if value < mid_val:
        return recursive_binary_search_sorted(sample_lst, left, mid - 1, value)
    if value > mid_val:
        return recursive_binary_search_sorted(sample_lst, mid + 1, right, value)


def iterative_binary_search_sorted(sample_lst, value):
    # Time complexity = O(log(n))
    # Space complexity = O(1)
    left = 0
    right = len(sample_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = sample_lst[mid]
        if mid_val == value:
            return mid
        if value < mid_val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def recursive_binary_search_rotated(sample_lst, left, right, value):
    # Time complexity = O(log(n))
    # Space complexity = O(log(n))
    mid = (left + right) // 2
    if left > right:
        return -1
    if sample_lst[mid] == value:
        return mid
    if sample_lst[left] <= sample_lst[mid]:
        if sample_lst[left] <= value <= sample_lst[mid]:
            return recursive_binary_search_rotated(sample_lst, left, mid - 1, value)
        else:
            return recursive_binary_search_rotated(sample_lst, mid + 1, right, value)
    else:
        if sample_lst[mid] <= value <= sample_lst[right]:
            return recursive_binary_search_rotated(sample_lst, mid + 1, right, value)
        else:
            return recursive_binary_search_rotated(sample_lst, left, mid - 1, value)


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

    sample7 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    print(recursive_binary_search_rotated(sample7, 0, len(sample7) - 1, 3))

    sample8 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    print(recursive_binary_search_rotated(sample8, 0, len(sample8) - 1, 100))

    sample9 = [3, 4, 5, 6, 7, 8, 9, 1, 2]
    print(recursive_binary_search_rotated(sample9, 0, len(sample9) - 1, 7))
