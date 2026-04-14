import uf


class WeightedQuickUnion(uf.UF):
    def __init__(self, number_of_elements):
        self._elements = [i for i in range(number_of_elements)]
        self._size = [1 for i in range(number_of_elements)]
        self._count = number_of_elements

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self._size[p_root] < self._size[q_root]:
            self._elements[p_root] = q_root
            self._size[q_root] += 1
        else:
            self._elements[q_root] = p_root
            self._size[p_root] += 1
        self._count -= 1

    def find(self, p):
        while p != self._elements[p]:
            p = self._elements[p]
        return p

    def count(self):
        return self._count

    def print(self):
        print(",".join([str(el) for el in self._elements]))
