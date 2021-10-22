def insertion_sort(sample_lst, reverse=False):
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    for index, item in enumerate(sample_lst[1:], start=1):
        pos = index
        while item < sample_lst[pos - 1] and pos > 0:
            sample_lst[pos] = sample_lst[pos - 1]
            pos -= 1
        sample_lst[pos] = item

    if reverse:
        sample_lst.reverse()


if __name__ == "__main__":
    sample1 = [2, 4, 3, 5, 1]
    insertion_sort(sample1)
    print(sample1)

    sample2 = [2, 2, 3, 4, 3]
    insertion_sort(sample2)
    print(sample2)

    nums = int(input("How many numbers you want to enter?: "))
    input_lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", input_lst)
    insertion_sort(input_lst)
    print("Ascending order:", input_lst)
