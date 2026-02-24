"""
24/02/2026
@author: Volodymyr Pohribnyi
"""
"""Basically, I took the Hoare partition method because it's faster 
than Lomuto. I tweaked it a bit so that if the numbers are the exact same, 
the pointers still move. Otherwise, it gets stuck in an infinite loop.
Also, I changed the sorting order. Bigger numbers go to the left, smaller to 
the right. Then it just recursively checks if we hit the target k. If the index 
is bigger than our target, we search the left part. If it's smaller, we go right. 
If they match, we found it! Also, k starts from 1, not 0. And if you pass an empty list,
it just returns None so the program doesn't crash."""
import time
import random
import sys


def partition(array, low, high):
    mid = low + (high - low) // 2

    if array[mid] <= array[low]:
        array[mid], array[low] = array[low], array[mid]
    if array[high] <= array[low]:
        array[high], array[low] = array[low], array[high]
    if array[high] <= array[mid]:
        array[high], array[mid] = array[mid], array[high]

    array[low], array[mid] = array[mid], array[low]

    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= high and array[i] >= pivot:
            i += 1
        while j > low and array[j] <= pivot:
            j -= 1
        if i >= j:
            array[low], array[j] = array[j], array[low]
            return j
        array[i], array[j] = array[j], array[i]


def kth_largest_element(array, low, high, k):
    if low == high:
        return array[low]

    if high > low:
        pi = partition(array, low, high)

        if pi + 1 > k:
            return kth_largest_element(array, low, pi - 1, k)
        elif pi + 1 < k:
            return kth_largest_element(array, pi + 1, high, k)
        else:
            return array[pi]
    return None


def generate_data(size):
    return list(range(0, size))


def generate_repetitive_data(size):
    arr = []
    ch = list(range(1, 10))
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
    first_el = int(size * 0.8)
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
        algorithms = [("K-th largest element", kth_largest_element)]
        ordinal = {1: "1-st", 2: "2-nd", 3: "3-rd"}
        ch = list(range(1, i + 1))

        if i == 0:
            for name, func in algorithms:
                data_copy = original_data
                n = len(data_copy)
                # Перевірка на порожній масив
                num = func(data_copy, 0, n - 1, i) if n > 0 else None
                print(f"{name}({i:_}): {num}\n")
            continue

        for name, func in algorithms:
            k = random.choice(ch)
            data_copy = original_data.copy()
            if i <= 10:
                print(f"Input array: {data_copy}")

            n = len(data_copy)
            print(f"{name}({i:_}): ", end="")
            start = time.time()
            num = func(data_copy, 0, n - 1, k)
            duration = time.time() - start
            print(f"{duration:.6f} сек")

            if k in ordinal:
                suffix = ordinal[k]
                print(f"{suffix} largest element is {num}\n")
            else:
                print(f"{k}-th largest element is {num}\n")


def test():
    sizes = [0, 1, 10, 100, 1_000, 10_000]

    run_benchmark("SORTED DATA", generate_data, sizes)
    run_benchmark("PARTIALLY SORTED DATA", generate_partially_sorted, sizes)
    run_benchmark("RANDOM DATA",
                  lambda s: generate_random_data(generate_data(s)),
                  sizes
    )
    run_benchmark(
        "RANDOM DATA WITH DUPLICATES",
        lambda s: generate_random_data(generate_repetitive_data(s)),
        sizes
    )
    run_benchmark("REVERSE DATA", generate_reverse_data, sizes)


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    test()