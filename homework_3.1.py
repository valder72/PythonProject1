def buble_sort (arr):

    for j in range(len(arr)-1):

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

if __name__ == "__main__":
    print(buble_sort([0,5,3,1,2]))
    for j in range(5):
        print(j)