
def partition(arr, lt, gt):
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
    if low >= high:
        return

    lt, gt = partition(a, low, high)

    quick_sort(a, low, lt)
    quick_sort(a, gt, high)

def generate_repetitive_data(size);


if __name__ == "__main__":
    pass
    # TODO add tests

