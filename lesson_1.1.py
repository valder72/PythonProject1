def binary_search(arr, tar):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == tar:
            return True
        elif arr[mid] < tar:
            low = mid + 1
        else:
            high = mid - 1
if __name__ == '__main__':
    count = 0
    N = [-4,-3,-2,-1, 0, 1, 2, 3, 4]
    for i in range(0, len(N)):
        for j in range(i + 1, len(N)):
            target = -(N[i] + N[j])
            if binary_search(N, target):
                count += 1
    print(count)

