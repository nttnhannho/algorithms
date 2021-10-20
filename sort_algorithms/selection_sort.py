def selection_sort(sample_lst, reverse=False):
    for index, item in enumerate(sample_lst[:-1]):
        if reverse:
            val = max(sample_lst[index:])
        else:
            val = min(sample_lst[index:])
        val_index = sample_lst.index(val, index)
        if index != val_index:
            sample_lst[index], sample_lst[val_index] = sample_lst[val_index], sample_lst[index]


def selection_sort_without_minmax(sample_lst, reverse=False):
    for index, item in enumerate(sample_lst[:-1]):
        if reverse:
            val = sample_lst[index]
            for subitem in sample_lst[index + 1:]:
                if subitem > val:
                    val = subitem
        else:
            val = sample_lst[index]
            for subitem in sample_lst[index + 1:]:
                if subitem < val:
                    val = subitem
        val_index = sample_lst.index(val, index)
        if index != val_index:
            sample_lst[index], sample_lst[val_index] = sample_lst[val_index], sample_lst[index]


if __name__ == "__main__":
    sample1 = [56, 3, 2, 78, 6, 0]
    selection_sort(sample1)
    print(sample1)

    sample2 = [56, 0, 2, 2, 6, 0]
    selection_sort(sample2)
    print(sample2)

    selection_sort_without_minmax(sample1)
    print(sample1)

    selection_sort_without_minmax(sample2)
    print(sample2)

    selection_sort_without_minmax(sample1, True)
    print(sample1)

    selection_sort_without_minmax(sample2, True)
    print(sample2)

    nums = int(input("How many numbers you want to enter?: "))
    lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", lst)
    selection_sort(lst)
    print("Ascending order:", lst)
