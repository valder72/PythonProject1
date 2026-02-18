"""
17/02/2026
@author: Volodymyr Pohribnyi
"""

import random
import time
import sys


def lomuto_partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def lomuto_quick_sort(array, low, high):
    if low < high:
        pi = lomuto_partition(array, low, high)
        lomuto_quick_sort(array, low, pi - 1)
        lomuto_quick_sort(array, pi + 1, high)


def hoare_partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= high and array[i] < pivot:
            i += 1
        while j > low and array[j] > pivot:
            j -= 1
        if i > j:
            array[low], array[j] = array[j], array[low]
            return j
        array[i], array[j] = array[j], array[i]


def hoare_quick_sort(array, low, high):
    if low < high:
        pi = hoare_partition(array, low, high)
        hoare_quick_sort(array, low, pi - 1)
        hoare_quick_sort(array, pi + 1, high)


def insertion_sort(array, lo, hi):
    for i in range(lo + 1, hi + 1):
        key = array[i]
        j = i - 1
        while j >= lo and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def better_hoare_partition(array, low, high):
    mid = low + (high - low) // 2

    if array[mid] < array[low]:
        array[mid], array[low] = array[low], array[mid]
    if array[high] < array[low]:
        array[high], array[low] = array[low], array[high]
    if array[high] < array[mid]:
        array[high], array[mid] = array[mid], array[high]

    array[low], array[mid] = array[mid], array[low]

    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= high and array[i] < pivot:
            i += 1
        while j > low and array[j] > pivot:
            j -= 1
        if i > j:
            array[low], array[j] = array[j], array[low]
            return j
        array[i], array[j] = array[j], array[i]


def better_hoare_quick_sort(array, low, high):
    if high - low + 1 <= 10:
        insertion_sort(array, low, high)
        return

    pi = better_hoare_partition(array, low, high)
    better_hoare_quick_sort(array, low, pi - 1)
    better_hoare_quick_sort(array, pi + 1, high)


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


def run_benchmark(label, data_generator, sizes):
    print(f"[{label}]\n")
    for i in sizes:
        print(f"----{i:_}----")

        original_data = data_generator(i)

        algorithms = [
            ("Lomuto quick sort", lomuto_quick_sort),
            ("Hoare quick sort", hoare_quick_sort),
            ("Better Hoare quick sort", better_hoare_quick_sort)
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
    run_benchmark("REVERSE DATA", generate_reverse_data, sizes)


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    test()
