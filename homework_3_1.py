from homework_3_2 import knuth_shuffle
import time

def bubble_sort (arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

def random_numbers(n):
    return knuth_shuffle(list(range(n-1)))

def test(size):
    print(bubble_sort(random_numbers(size//100)))

    x = random_numbers(size)
    start = time.time()
    bubble_sort(x)
    print(time.time() - start)

    x = random_numbers(size)
    start = time.time()
    bubble_sort(x)
    print(time.time() - start)

    x = random_numbers(size)
    start = time.time()
    bubble_sort(x)
    print(time.time() - start)

if __name__ == "__main__":
    test(20000)