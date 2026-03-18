class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value} -> {self.next}"


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.st = [None] * self.slots
        self.number_of_taken_slots = 0

    def __str__(self):
        return "  |  ".join(map(str, self.st))

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value) -> ListNode:
        """
        :param key:
        :param value:
        :return:
        """
        k_hash = self.hash_function(key)

        if self.st[k_hash] is None:
            node = ListNode(key, value)
            self.st[k_hash] = node
            return node

        else:
            current_node = self.st[k_hash]
            while current_node:
                if key == current_node.key:
                    current_node.value = value
                    return current_node
                current_node = current_node.next
            node = ListNode(key, value)
            tail = self.st[k_hash]
            node.next =  tail
            self.st[k_hash] = node
            return node




    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        pass


if __name__ == '__main__':
    obj = MyHashTable()
    obj.put("1", 1)
    obj.put("1", 2)
    obj.put("2", 27)
    obj.put("3", 12)
    obj.put("4", 2)
    obj.put("14", 22)
    obj.put("24", 2)

    print(obj)
    print(obj.get("1"))
    print(obj.get("14"))
    print(obj.get("24"))

    obj.remove("1")
    obj.remove("2")
    obj.remove("14")
    print(obj)