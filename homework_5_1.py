"""
https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/
python3 program for 3-way quick sort
# this code is contributed by aditya942003patil and fixed by Oleksandra Radziievska
"""
import time
import random
import sys


# It uses Dutch National Flag Algorithm
def partition(arr, lt, gt):
    """
    This function partitions a[] in three parts
    a) a[l..i] contains all elements smaller than pivot
    b) a[i+1..j-1] contains all occurrences of pivot
    c) a[j..r] contains all elements greater than pivot
    """
    # To handle 2 elements
    if gt - lt <= 1:
        if arr[gt] < arr[lt]:
            arr[gt], arr[lt] = arr[lt], arr[gt]
        return lt, gt

    i = lt
    pivot = arr[gt]
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] == pivot:
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
    return lt - 1, i


# 3-way partition based quick sort
def quick_sort(a, low, high):
    if low >= high:  # 1 or 0 elements
        return

    # Note that i and j are passed as reference
    lt, gt = partition(a, low, high)

    # Recur two halves
    quick_sort(a, low, lt)
    quick_sort(a, gt, high)


def generate_data(size):
    return list(range(0, size))


def generate_repetitive_data(size):
    arr = []
    ch = list(range(1, 51))

    for _ in range(0, size):
        r = random.choice(ch)
        arr.append(r)
    return arr


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


def run_benchmark(label, data_generator, sizes):
    print(f"[{label}]\n")
    for i in sizes:
        print(f"----{i:_}----")

        original_data = data_generator(i)

        algorithms = [
            ("Quick sort", quick_sort)
        ]

        for name, func in algorithms:
            data_copy = original_data.copy()
            n = len(data_copy)
            print(f"{name}({i:_}): ", end="")
            start = time.time()
            func(data_copy, 0, n - 1)
            print(f"{time.time() - start:.6f} сек\n")


def test():
    sizes = [100, 1_000, 10_000]

    run_benchmark("SORTED DATA", generate_data, sizes)
    run_benchmark("PARTIALLY SORTED DATA", generate_partially_sorted, sizes)
    run_benchmark("RANDOM DATA", lambda s: generate_random_data(generate_data(s)), sizes)
    run_benchmark("RANDOM DATA WITH DUPLICATES", lambda s: generate_random_data(generate_repetitive_data(s)), sizes)
    run_benchmark("REVERSE DATA", generate_reverse_data, sizes)


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    test()
