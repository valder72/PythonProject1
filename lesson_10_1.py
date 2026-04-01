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
        self.max_load_factor = 0.75
        self.min_load_factor = 0.25
        self.st = [None] * self.slots
        self.taken_slots = 0

    def __str__(self):
        return "  |  ".join(map(str, self.st))

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value):
        self._put(key, value)
        self.rehashing()

    def _put(self, key, value) -> ListNode:
        """
        :param key:
        :param value:
        :return:
        """
        k_hash = self.hash_function(key)

        if self.st[k_hash] is None:
            node = ListNode(key, value)
            self.st[k_hash] = node
            self.taken_slots += 1
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
            self.taken_slots += 1
            return node

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """
        k_hash = self.hash_function(key)
        data_node = self.st[k_hash]

        if data_node is None:
            return None

        while data_node is not None:
            if key == data_node.key:
                return data_node
            data_node = data_node.next

        return None

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """
        k_hash = self.hash_function(key)
        data_node = self.st[k_hash]
        current_data_node = data_node.next

        if key == data_node.key:
            self.st[k_hash] = data_node.next
            data_node.next = None
            return (data_node.key, data_node.value)

        while current_data_node is not None:
            if key == current_data_node.key:
                data_node.next = current_data_node.next
                current_data_node.next = None
                return (current_data_node.key, current_data_node.value)
            data_node = data_node.next
            current_data_node = current_data_node.next
        return None

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        if self.taken_slots / self.slots >= self.max_load_factor:
            self.slots *= 2
            self._resize()
        elif self.taken_slots / self.slots <= self.min_load_factor and self.slots > 10:
            self.slots //= 2
            self._resize()

    def _resize(self):
        old_head = self.head
        self.head = [None] * self.slots
        self.taken_slots = 0

        for item in old_head:
            while item is not None:
                self.put(item.key, item.value)
                item = item.next

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