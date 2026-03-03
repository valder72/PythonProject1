class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class KeyValueBST:
    def __init__(self):
        self._root = None

    def _size(self, node):
        if node is None:
            return 0
        return node.count

    def size(self, lo=None, hi=None):
        if lo is None and hi is None:
            return self._size(self._root)

        if lo is not None and hi is not None:
            if lo > hi:
                return 0
            if self.contains(hi):
                return self.rank(hi) - self.rank(lo) + 1
            else:
                return self.rank(hi) - self.rank(lo)
        return 0

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        x = self._root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        self._root = self._put_el(self._root, key, val)

    def _put_el(self, node, key, val):
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self._put_el(node.left, key, val)
        elif key > node.key:
            node.right = self._put_el(node.right, key, val)
        else:
            node.val = val

        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def min(self):
        if self._root is None:
            return None
        return self._min(self._root).key

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self):
        if self._root is None:
            return None
        return self._max(self._root).key

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def floor(self, key):
        node = self._floor(self._root, key)
        if node is None:
            return None
        return node.key

    def _floor(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        t = self._floor(node.right, key)
        if t is not None:
            return t
        return node

    def ceiling(self, key):
        node = self._ceiling(self._root, key)
        if node is None:
            return None
        return node.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key > node.key:
            return self._ceiling(node.right, key)
        t = self._ceiling(node.left, key)
        if t is not None:
            return t
        return node

    def rank(self, key):
        return self._rank(key, self._root)

    def _rank(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def select(self, k):
        if k < 0 or k >= self.size():
            return None
        node = self._select(self._root, k)
        return node.key if node else None

    def _select(self, node, k):
        if node is None:
            return None
        t = self._size(node.left)
        if t > k:
            return self._select(node.left, k)
        elif t < k:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def delete_min(self):
        if self._root is not None:
            self._root = self._delete_min(self._root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete_max(self):
        if self._root is not None:
            self._root = self._delete_max(self._root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left
        node.right = self._delete_max(node.right)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        self._root = self._delete(self._root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left

        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def keys(self, lo=None, hi=None):
        if lo is None and hi is None:
            lo = self.min()
            hi = self.max()

        queue = []
        if lo is not None and hi is not None:
            self._keys(self._root, queue, lo, hi)
        return queue

    def _keys(self, node, queue, lo, hi):
        if node is None:
            return
        if lo < node.key:
            self._keys(node.left, queue, lo, hi)
        if lo <= node.key <= hi:
            queue.append(node.key)
        if hi > node.key:
            self._keys(node.right, queue, lo, hi)

    def __iter__(self):
        self._iterable = self.keys()
        self._iterable_el = 0
        return self

    def __next__(self):
        if self._iterable_el < len(self._iterable):
            res = self._iterable[self._iterable_el]
            self._iterable_el += 1
            return res
        else:
            raise StopIteration


def test():
    print("--- Початок тестування ---")
    bst = KeyValueBST()

    assert bst.is_empty(), "Дерево має бути порожнім при створенні"
    assert bst.size() == 0, "Розмір порожнього дерева має бути 0"

    data = [
        (10, "десять"), (4, "чотири"), (15, "п'ятнадцять"),
        (2, "два"), (8, "вісім"), (12, "дванадцять"), (20, "двадцять")
    ]
    for k, v in data:
        bst.put(k, v)

    assert not bst.is_empty(), "Дерево не порожнє після вставок"
    assert bst.size() == 7, "Розмір має бути 7"

    assert bst.get(8) == "вісім", "Пошук значення за ключем 8"
    assert bst.get(99) is None, "Пошук неіснуючого ключа повертає None"

    assert bst.contains(15), "contains для існуючого ключа"
    assert not bst.contains(99), "contains для неіснуючого ключа"

    assert bst.min() == 2, "Мінімальний ключ має бути 2"
    assert bst.max() == 20, "Максимальний ключ має бути 20"

    assert bst.floor(9) == 8, "Найбільший ключ <= 9 має бути 8"
    assert bst.ceiling(9) == 10, "Найменший ключ >= 9 має бути 10"

    assert bst.rank(10) == 3, "Кількість ключів < 10 має бути 3 (це 2, 4, 8)"
    assert bst.select(3) == 10, "Елемент з індексом 3 (4-й найменший) має бути 10"

    assert bst.size(5, 15) == 4, "Кількість ключів від 5 до 15: 4 штуки (8, 10, 12, 15)"
    assert bst.keys(5, 15) == [8, 10, 12, 15], "Список ключів в діапазоні [5, 15]"

    keys_from_iter = [k for k in bst]
    assert keys_from_iter == [2, 4, 8, 10, 12, 15, 20], "Ітератор має повертати відсортовані ключі"

    bst.delete_min()
    assert bst.min() == 4, "Після delete_min новим мінімумом має стати 4"
    assert bst.size() == 6, "Розмір після видалення зменшився на 1"

    bst.delete_max()
    assert bst.max() == 15, "Після delete_max новим максимумом має стати 15"

    bst.delete(10)
    assert not bst.contains(10), "Ключ 10 має бути видалений"
    assert bst.size() == 4, "Розмір після всіх видалень має бути 4"

    print("--- Усі тести пройдено успішно! ---")


if __name__ == '__main__':
    test()