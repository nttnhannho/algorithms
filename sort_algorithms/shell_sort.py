def shell_sort(sample_lst, reverse=False):
    # Time complexity = O(n*(log(n))^2)
    # Space complexity = O(1)
    # In-place algorithm
    # Unstable
    gap = len(sample_lst) // 2
    while gap > 0:
        for index, item in enumerate(sample_lst[gap:], start=gap):
            pos = index
            while pos >= gap and item < sample_lst[pos - gap]:
                sample_lst[pos] = sample_lst[pos - gap]
                pos -= gap
            sample_lst[pos] = item
        gap = gap // 2

    if reverse:
        sample_lst.reverse()


if __name__ == "__main__":
    sample1 = [2, 4, 3, 5, 1]
    shell_sort(sample1)
    print(sample1)

    sample2 = [2, 2, 3, 4, 3]
    shell_sort(sample2)
    print(sample2)

    sample3 = [2, 4, 3, 5, 1]
    shell_sort(sample3, True)
    print(sample3)

    sample4 = [2, 2, 3, 4, 3]
    shell_sort(sample4, True)
    print(sample4)

    nums = int(input("How many numbers you want to enter?: "))
    input_lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", input_lst)
    shell_sort(input_lst)
    print("Ascending order:", input_lst)
