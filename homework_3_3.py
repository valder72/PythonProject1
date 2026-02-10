from homework_3_2 import knuth_shuffle

def random_list(size):
    return knuth_shuffle(list(range(size)))

def get_inversion(arr):
    output = []
    n = len(arr)

    for i in range(n):
        j = i + 1
        for j in range (i + 1, n):
            if arr[j] < arr[i]:
                output.append((arr[i], arr[j]))

    return output

def is_partially_sorted(arr, k):
    return len(get_inversion(arr)) < k * len(arr)

def test_inversion(size):
    print(get_inversion(random_list(size)))

def test_partially_sorted(size, k):
    print(is_partially_sorted(random_list(size), k))


if __name__ == "__main__":
    test_inversion(20)
    test_inversion(100)
    test_partially_sorted(20, 5)
    test_partially_sorted(100, 20)
