import random
import time

def generate_data(n):
    return list(range(n))

def simple_shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def knuth_shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def test_simple_shuffle(size):
    start = time.time()
    simple_shuffle(generate_data(size))
    print(time.time() - start)

    start = time.time()
    simple_shuffle(generate_data(size))
    print(time.time() - start)

    start = time.time()
    simple_shuffle(generate_data(size))
    print(time.time() - start)

def test_knuth_shuffle(size):
    start = time.time()
    knuth_shuffle(generate_data(size))
    print(time.time() - start)

    start = time.time()
    knuth_shuffle(generate_data(size))
    print(time.time() - start)

    start = time.time()
    knuth_shuffle(generate_data(size))
    print(time.time() - start)

if __name__ == "__main__":
    size = 20000
    test_simple_shuffle(size)
    test_knuth_shuffle(size)