def bubble_sort(sample_lst, reverse=False):
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    # In-place algorithm
    # Stable
    for exec_time in range(len(sample_lst) - 1, 0, -1):
        swapped = False
        for index in range(exec_time):
            if sample_lst[index] > sample_lst[index + 1]:
                sample_lst[index], sample_lst[index + 1] = sample_lst[index + 1], sample_lst[index]
                swapped = True
        if not swapped:
            break

    if reverse:
        sample_lst.reverse()


if __name__ == "__main__":
    sample1 = [10, 15, 4, 23, 0]
    bubble_sort(sample1)
    print(sample1)

    sample2 = [10, 15, 10, 15, 0]
    bubble_sort(sample2)
    print(sample2)

    sample3 = [10, 15, 4, 23, 0]
    bubble_sort(sample3, True)
    print(sample3)

    sample4 = [10, 15, 10, 15, 0]
    bubble_sort(sample4, True)
    print(sample4)

    sample5 = [1, 2, 3, 4, 5]
    bubble_sort(sample5, True)
    print(sample5)

    nums = int(input("How many numbers you want to enter?: "))
    lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", lst)
    bubble_sort(lst)
    print("Ascending order:", lst)
