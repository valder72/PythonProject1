def union_and_intersection(arr1, arr2):
    union = []
    intersection = []

    first = len(arr1)
    second = len(arr2)

    i = 0
    j = 0
    while i < first and j < second:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1

        else:
            union.append(arr1[i])
            i += 1

    while i < first:
        union.append(arr1[i])
        i += 1

    while j < second:
        union.append(arr2[j])
        j += 1

    i = 0
    j = 0
    while i < first and j < second:
        if arr1[i] < arr2[j]:
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1

        else:
            intersection.append(arr1[i])
            i += 1
            j += 1

    return union, intersection

if __name__ == '__main__':
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    u, i = union_and_intersection(arr1, arr2)
    print(f"Union: {u}\nIntersection: {i}\n")

    arr1 = [2, 5, 6]
    arr2 = [4, 6, 8, 10]
    u, i = union_and_intersection(arr1, arr2)
    print(f"Union: {u}\nIntersection: {i}\n")

    arr1 = [2, 2, 5, 6]
    arr2 = [2, 2, 4, 5, 5, 6, 8, 10]
    u, i = union_and_intersection(arr1, arr2)
    print(f"Union: {u}\nIntersection: {i}")