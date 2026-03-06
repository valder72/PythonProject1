from collections import deque

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        return f"{self.key}: {self.val} ({self.left}, {self.right})"


class BST:
    def __init__(self):
        self._root = None

    def __iter__(self):
        self._iterable = deque()
        self._iterable_el = 0
        self._inorder(self._root)
        return self

    def __next__(self):
        if self._iterable_el < len(self._iterable):
            self._iterable_el += 1
            return self._iterable[self._iterable_el - 1]
        else:
            raise StopIteration

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        self._iterable.append(node.key)
        self._inorder(node.right)

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

    def min(self):
        temp = self._root
        if temp is None:
            return None
        while temp.left is not None:
            temp = temp.left
        return temp.val

    def max(self):
        temp = self._root
        if temp is None:
            return None
        while temp.right is not None:
            temp = temp.right
        return temp.val

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

    def size(self):
        return self._size(self._root)

    @staticmethod
    def _size(node):
        if node is None:
            return 0
        return node.count

    def rank(self, key):
        return self._rank(key, self._root)

    def _rank(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(key, node.left)
        if key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def delete_min(self):
        if self._root is None:
            return
        self._root = self._delete_min(self._root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    @staticmethod
    def _min_node(node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        if self._root is None:
            return
        self._root = self._delete(self._root, key)

    def _delete(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min_node(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x


if __name__ == "__main__":
    bst = BST()
    bst.put(1, "Andrii")
    bst.put(10, "Ivan")
    bst.put(2, "Ira")
    bst.put(15, "Vita")
    bst.put(20, "Petro")
    bst.put(-10, "Mykola")
    print(f'Size: {bst.size()}')
    print(bst.get(5))
    print(bst.get(15))
    print('elements: ')
    for e in bst:
        print(e)
    print(bst.min())
    print(bst.max())
    print(bst.floor(11))
    print(bst.size())
    print(bst.rank(3))
    bst.delete(-1)
    print('elements: ')
    for e in bst:
        print(e)
