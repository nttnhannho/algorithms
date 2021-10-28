from search_algorithms.binary_search import recursive_binary_search_sorted


def recursive_exponential_search(sample_lst, length, value):
    # Time complexity = O(log(n))
    # Space complexity = O(log(n))
    if sample_lst[0] == value:
        return 0

    index = 1
    while index < length and sample_lst[index] <= value:
        index *= 2

    return recursive_binary_search_sorted(sample_lst, index // 2, min(index, length - 1), value)


if __name__ == "__main__":
    sample1 = [1, 2, 3, 4, 5, 6, 7]
    for i in range(1, len(sample1) + 1):
        print(recursive_exponential_search(sample1, len(sample1), i))

    sample2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(recursive_exponential_search(sample2, len(sample2), 100))
