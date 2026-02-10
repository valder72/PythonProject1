"""
10/02/2026
@author: Volodymyr Pohribnyi
"""
import random
import time

def insertion_sort(array, lo, hi):
    for i in range(lo + 1, hi + 1):
        key = array[i]
        j = i - 1

        while j >= lo and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

def merge(arr, lo, mid, hi):
    """
    :param arr: array we need to merge
    :param lo: (low) the index of the first subarray beginning
    :param mid: middle index
    :param hi: (high) the index of the second subarray ending
    :return:
    """

    # create temp arrays and copy data to them
    left = arr[lo:(mid + 1)]
    right = arr[(mid + 1):(hi + 1)]

    left_count = len(left)
    right_count = len(right)

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray (left)
    j = 0  # Initial index of second subarray (right)
    k = lo  # Initial index of merged subarray

    while i < left_count and j < right_count:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of first subarray, if there are any
    while i < left_count:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of second subarray, if there are any
    while j < right_count:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, lo, hi):
    """
    :param arr: array we need to sort
    :param lo: (low) the left index
    :param hi: (high) the right index
    :return:
    """
    if lo < hi:
        # Same as (l_ind + r_ind) // 2, but avoids overflow for large l_ind and r_ind
        mid = lo + (hi - lo) // 2

        # Sort first and second halves
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)
        merge(arr, lo, mid, hi)


def better_merge(arr, lo, mid, hi):
    """
    :param arr: array we need to merge
    :param lo: (low) the index of the first subarray beginning
    :param mid: middle index
    :param hi: (high) the index of the second subarray ending
    :return:
    """
    if arr[mid] <= arr[mid + 1]:
        return

    # create temp arrays and copy data to them
    left = arr[lo:(mid + 1)]
    right = arr[(mid + 1):(hi + 1)]

    left_count = len(left)
    right_count = len(right)

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray (left)
    j = 0  # Initial index of second subarray (right)
    k = lo  # Initial index of merged subarray

    while i < left_count and j < right_count:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of first subarray, if there are any
    while i < left_count:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of second subarray, if there are any
    while j < right_count:
        arr[k] = right[j]
        j += 1
        k += 1


def improved_merge_sort(arr, lo, hi):
    """
    :param arr: array we need to sort
    :param lo: (low) the left index
    :param hi: (high) the right index
    :return:
    """
    if lo < hi:
        if hi - lo + 1 <= 7:
            insertion_sort(arr, lo, hi)
            return

        # Same as (l_ind + r_ind) // 2, but avoids overflow for large l_ind and r_ind
        mid = lo + (hi - lo) // 2

        # Sort first and second halves
        improved_merge_sort(arr, lo, mid)
        improved_merge_sort(arr, mid + 1, hi)

        better_merge(arr, lo, mid, hi)

def generate_data(size):
    return list(range(0, size))

def generate_random_data(arr):
    for i in range(len(arr)):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]

    return arr

def generate_partially_sorted(size):
    first_el = int(size * 0.9)
    second_el = list(range(first_el, size))
    generate_random_data(second_el)

    return list(range(0, first_el)) + second_el

def generate_reverse_data(size):
    return list(range(size, -1, -1))

def test():
    size = [100, 1_000, 10_000, 100_000, 1_000_000]

    print("Merge:\n")

    for i in size:
        print(f"Sorted data({i}): ", end="")
        data = generate_data(i)
        n = len(data)
        start = time.time()
        merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Partially sorted data({i}): ", end="")
        data = generate_partially_sorted(i)
        n = len(data)
        start = time.time()
        merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Random data({i}): ", end="")
        sorted_data = generate_data(i)
        data = generate_random_data(sorted_data)
        n = len(data)
        start = time.time()
        merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Reverse data({i}): ", end="")
        data = generate_reverse_data(i)
        n = len(data)
        start = time.time()
        merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\nImproved merge:\n")

    for i in size:
        print(f"Sorted data({i}): ", end="")
        data = generate_data(i)
        n = len(data)
        start = time.time()
        improved_merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Partially sorted data({i}): ", end="")
        data = generate_partially_sorted(i)
        n = len(data)
        start = time.time()
        improved_merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Random data({i}): ", end="")
        sorted_data = generate_data(i)
        data = generate_random_data(sorted_data)
        n = len(data)
        start = time.time()
        improved_merge_sort(data, 0, n - 1)
        print(time.time() - start)

    print("\n\n")

    for i in size:
        print(f"Reverse data({i}): ", end="")
        data = generate_reverse_data(i)
        n = len(data)
        start = time.time()
        improved_merge_sort(data, 0, n - 1)
        print(time.time() - start)


if __name__ == '__main__':
    test()