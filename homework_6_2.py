class HeapSort:
    def __init__(self, elements):
        self._elements = [None] + elements
        self._capacity = len(elements)

        # build the heap
        k = self._capacity // 2
        while k >= 1:
            self._sink(k)
            k -= 1

        # "delete" the max element at each iteration
        while self._capacity > 1:
            self._exch(1, self._capacity)
            self._capacity -= 1
            self._sink(1)

    def sorted(self):
        return self._elements[1:]

    def _sink(self, k):
        while 2 * k <= self._capacity:
            j = 2 * k
            if j < self._capacity and self._less(j, j + 1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def _exch(self, k, j):
        self._elements[k], self._elements[j] = self._elements[j], self._elements[k]

    def _less(self, i, j):
        return self._elements[i] < self._elements[j]


if __name__ == "__main__":
    arr = [1, 12, 9, 5, 6, 10]
    heapSort = HeapSort(arr)
    result = heapSort.sorted()
    print("Sorted array is")
    print(result)
