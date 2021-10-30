import random
from statistics import median


def pivot_place_as_first(sample_lst, first, last):
    pivot = sample_lst[first]
    left = first + 1
    right = last
    while True:
        while left <= right and sample_lst[left] <= pivot:
            left += 1
        while left <= right and sample_lst[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            sample_lst[left], sample_lst[right] = sample_lst[right], sample_lst[left]
    sample_lst[first], sample_lst[right] = sample_lst[right], sample_lst[first]
    return right


def pivot_place_as_last(sample_lst, first, last):
    pivot = sample_lst[last]
    left = first
    right = last - 1
    while True:
        while left <= right and sample_lst[left] <= pivot:
            left += 1
        while left <= right and sample_lst[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            sample_lst[left], sample_lst[right] = sample_lst[right], sample_lst[left]
    sample_lst[last], sample_lst[left] = sample_lst[left], sample_lst[last]
    return left


def pivot_place_as_random(sample_lst, first, last):
    rindex = random.randint(first, last)
    sample_lst[rindex], sample_lst[last] = sample_lst[last], sample_lst[rindex]
    pivot = sample_lst[last]
    left = first
    right = last - 1
    while True:
        while left <= right and sample_lst[left] <= pivot:
            left += 1
        while left <= right and sample_lst[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            sample_lst[left], sample_lst[right] = sample_lst[right], sample_lst[left]
    sample_lst[last], sample_lst[left] = sample_lst[left], sample_lst[last]
    return left


def pivot_place_as_median(sample_lst, first, last):
    low = sample_lst[first]
    high = sample_lst[last]
    mid = (first + last) // 2
    pivot_val = median([low, sample_lst[mid], high])
    if pivot_val == low:
        pindex = first
    elif pivot_val == high:
        pindex = last
    else:
        pindex = mid
    sample_lst[pindex], sample_lst[last] = sample_lst[last], sample_lst[pindex]
    pivot = sample_lst[last]
    left = first
    right = last - 1
    while True:
        while left <= right and sample_lst[left] <= pivot:
            left += 1
        while left <= right and sample_lst[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            sample_lst[left], sample_lst[right] = sample_lst[right], sample_lst[left]
    sample_lst[last], sample_lst[left] = sample_lst[left], sample_lst[last]
    return left


def quick_sort(sample_lst, first, last, reverse=False):
    # Time complexity = O(n*log(n))
    # Space complexity = O(log(n))
    # In-place algorithm
    # Unstable
    if first < last:
        # as: first, last, random, median
        p = pivot_place_as_median(sample_lst, first, last)
        quick_sort(sample_lst, first, p - 1)
        quick_sort(sample_lst, p + 1, last)

    if reverse:
        sample_lst.reverse()


if __name__ == "__main__":
    sample1 = [56, 26, 93, 17, 31, 44]
    quick_sort(sample1, 0, len(sample1) - 1)
    print(sample1)

    sample2 = [56, 26, 26, 56, 31, 44]
    quick_sort(sample2, 0, len(sample2) - 1)
    print(sample2)

    sample3 = [56, 26, 93, 17, 31, 44]
    quick_sort(sample3, 0, len(sample1) - 1, True)
    print(sample3)

    sample4 = [56, 26, 26, 56, 31, 44]
    quick_sort(sample4, 0, len(sample2) - 1, True)
    print(sample4)

    nums = int(input("How many numbers you want to enter?: "))
    input_lst = [int(input("Enter number: ")) for num in range(nums)]
    print("Unsorted list", input_lst)
    quick_sort(input_lst, 0, len(input_lst) - 1)
    print("Ascending order:", input_lst)
