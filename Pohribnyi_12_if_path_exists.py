from typing import List


class WeightedQuickUnion:
    def __init__(self, number_of_elements: int):
        self._elements = [i for i in range(number_of_elements)]
        self._size = [1 for _ in range(number_of_elements)]
        self._count = number_of_elements

    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self._size[p_root] < self._size[q_root]:
            self._elements[p_root] = q_root
            self._size[q_root] += self._size[p_root]
        else:
            self._elements[q_root] = p_root
            self._size[p_root] += self._size[q_root]

        self._count -= 1

    def find(self, p: int) -> int:
        while p != self._elements[p]:
            p = self._elements[p]
        return p

    def count(self) -> int:
        return self._count

    def print(self):
        print(",".join([str(el) for el in self._elements]))


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        w = WeightedQuickUnion(n)
        for u, v in edges:
            w.union(u, v)
        return w.find(source) == w.find(destination)


def test_solution():
    sol = Solution()

    assert sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False
    assert sol.validPath(1, [], 0, 0) is True
    assert sol.validPath(4, [[0, 1], [2, 3]], 0, 3) is False
    assert sol.validPath(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 0, 4) is True
    assert sol.validPath(5, [[0, 1], [1, 2], [3, 4]], 0, 4) is False
    assert sol.validPath(4, [[0, 1], [0, 2], [0, 3]], 1, 3) is True
    assert sol.validPath(4, [], 0, 3) is False
    assert sol.validPath(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], 1, 4) is True
    assert sol.validPath(10, [], 5, 5) is True
    assert sol.validPath(10, [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6], [7, 8]], 0, 3) is True
    assert sol.validPath(10, [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6], [7, 8]], 0, 5) is False


if __name__ == "__main__":
    test_solution()