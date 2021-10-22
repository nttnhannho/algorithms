def selection_sort(sample_lst, reverse=False):
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    for index, item in enumerate(sample_lst[:-1]):
        val = min(sample_lst[index:])
        val_index = sample_lst.index(val, index)
        if sample_lst[index] != sample_lst[val_index]:  # Unstable -> Stable condition
            sample_lst[index], sample_lst[val_index] = sample_lst[val_index], sample_lst[index]

    if reverse:
        sample_lst.reverse()


def selection_sort_without_minmax(sample_lst, reverse=False):
    for index, item in enumerate(sample_lst[:-1]):
        val = sample_lst[index]
        for subitem in sample_lst[index + 1:]:
            if subitem < val:
                val = subitem
        val_index = sample_lst.index(val, index)
        if sample_lst[index] != sample_lst[val_index]:  # Unstable -> Stable condition
            sample_lst[index], sample_lst[val_index] = sample_lst[val_index], sample_lst[index]

    if reverse:
        sample_lst.reverse()


if __name__ == "__main__":
    sample1 = [56, 3, 2, 78, 6, 0]
    selection_sort(sample1)
    print(sample1)

    sample2 = [56, 0, 2, 2, 6, 0]
    selection_sort(sample2)
    print(sample2)

    sample3 = [56, 3, 2, 78, 6, 0]
    selection_sort(sample3, True)
    print(sample3)

    sample4 = [56, 0, 2, 2, 6, 0]
    selection_sort(sample4, True)
    print(sample4)

    sample5 = [56, 3, 2, 78, 6, 0]
    selection_sort_without_minmax(sample5)
    print(sample5)

    sample6 = [56, 0, 2, 2, 6, 0]
    selection_sort_without_minmax(sample6)
    print(sample6)

    sample7 = [56, 3, 2, 78, 6, 0]
    selection_sort_without_minmax(sample7, True)
    print(sample7)

    sample8 = [56, 0, 2, 2, 6, 0]
    selection_sort_without_minmax(sample8, True)
    print(sample8)

    nums = int(input("How many numbers you want to enter?: "))
    lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", lst)
    selection_sort(lst)
    print("Ascending order:", lst)
