def get_inversion(arr):
    output = []
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[i]:
                output.append((arr[i], arr[j]))
            j += 1
    return output

def is_partially_sorted(arr, k):
    if not arr:
        return True

    inversion = get_inversions(arr)
    return len(inversion) <= k * len(arr)

if __name__ == "__main__":
    array = [8,3,9,4,5,1]
    print(inversion(array))

#TODO доробити тести та частково впорядкований масив