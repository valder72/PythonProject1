"""
https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/
python3 program for 3-way quick sort
# this code is contributed by aditya942003patil and fixed by Oleksandra Radziievska
"""


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


if __name__ == "__main__":
    data = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4, 3, 4, 5, 3, 2, 2]
    print(data)

    quick_sort(data, 0, len(data) - 1)
    print(data)
