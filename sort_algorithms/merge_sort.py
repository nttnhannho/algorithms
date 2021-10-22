def merge_sort(lst, reverse=False):
    # Time complexity = O(nlogn)
    # Space complexity = O(n)
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        list_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                lst[list_index] = left[left_index]
                left_index += 1
            else:
                lst[list_index] = right[right_index]
                right_index += 1
            list_index += 1

        while left_index < len(left):
            lst[list_index] = left[left_index]
            left_index += 1
            list_index += 1

        while right_index < len(right):
            lst[list_index] = right[right_index]
            right_index += 1
            list_index += 1

    if reverse:
        lst.reverse()


if __name__ == "__main__":
    sample1 = [10, 15, 4, 23, 0]
    merge_sort(sample1)
    print(sample1)

    sample2 = [10, 15, 10, 15, 0]
    merge_sort(sample2)
    print(sample2)

    sample3 = [10, 15, 4, 23, 0]
    merge_sort(sample3, True)
    print(sample3)

    sample4 = [10, 15, 10, 15, 0]
    merge_sort(sample4, True)
    print(sample4)

    nums = int(input("How many numbers you want to enter?: "))
    input_lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", input_lst)
    merge_sort(input_lst)
    print("Ascending order:", input_lst)
