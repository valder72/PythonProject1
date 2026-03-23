"""
23/03/2026
@author: Volodymyr Pohribnyi
"""


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.max_load_factor = 0.5
        self.min_load_factor = 0.25
        self.head = [None] * self.slots
        self.taken_slots = 0

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value):
        self._rehashing()
        self._put(key, value)

    def _put(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        hash_el = self.hash_function(key)
        data = (key, value)

        while True:
            if self.head[hash_el] is None:
                self.head[hash_el] = data
                self.taken_slots += 1
                break
            elif self.head[hash_el][0] == key:
                self.head[hash_el] = data
                break

            hash_el += 1
            if hash_el == self.slots:
                hash_el = 0

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """
        hash_el = self.hash_function(key)
        start_hash = hash_el

        while self.head[hash_el] is not None:
            if self.head[hash_el][0] == key:
                return self.head[hash_el][1]

            hash_el += 1
            if hash_el == self.slots:
                hash_el = 0
            if hash_el == start_hash:
                break

        return None

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """
        hash_el = self.hash_function(key)
        start_hash = hash_el

        while self.head[hash_el] is not None:
            if self.head[hash_el][0] == key:
                removed_data = self.head[hash_el]
                self.head[hash_el] = None
                self.taken_slots -= 1

                hash_el += 1
                if hash_el == self.slots:
                    hash_el = 0

                while self.head[hash_el] is not None:
                    data_to_rehash = self.head[hash_el]
                    self.head[hash_el] = None
                    self.taken_slots -= 1
                    self._put(data_to_rehash[0], data_to_rehash[1])

                    hash_el += 1
                    if hash_el == self.slots:
                        hash_el = 0

                self._rehashing()
                return removed_data

            hash_el += 1
            if hash_el == self.slots:
                hash_el = 0
            if hash_el == start_hash:
                break

        return None

    def _rehashing(self):
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
            if item is not None:
                self._put(item[0], item[1])


if __name__ == '__main__':
    ht = MyHashTable()

    ht.put("apple", 100)
    ht.put("banana", 200)
    assert ht.get("apple") == 100, "Error: Неправильне значення для 'apple'"
    assert ht.get("banana") == 200, "Error: Неправильне значення для 'banana'"
    assert ht.get("orange") is None, "Error: 'orange' має повертати None"

    ht.put("apple", 999)
    assert ht.get("apple") == 999, "Error: Значення 'apple' не оновилося"
    assert ht.taken_slots == 2, "Error: Кількість слотів має бути 2 після оновлення"

    ht.put(0, "A")
    ht.put(10, "B")
    ht.put(20, "C")
    assert ht.get(0) == "A", "Error: Не знайдено ключ 0"
    assert ht.get(10) == "B", "Error: Не знайдено ключ 10 (колізія)"
    assert ht.get(20) == "C", "Error: Не знайдено ключ 20 (колізія)"

    removed = ht.remove(0)
    assert removed == (0, "A"), "Error: Метод remove повернув неправильні дані"
    assert ht.get(0) is None, "Error: Ключ 0 все ще існує після видалення"

    assert ht.get(10) == "B", "Error: Ключ 10 загубився після видалення 0"
    assert ht.get(20) == "C", "Error: Ключ 20 загубився після видалення 0"

    initial_slots = ht.slots
    for i in range(15):
        ht.put(f"key_{i}", i)

    assert ht.slots > initial_slots, "Error: Таблиця не розширилась після масового додавання"
    assert ht.get("key_10") == 10, "Error: Старі дані недоступні після розширення"

    expanded_slots = ht.slots
    for i in range(15):
        ht.remove(f"key_{i}")

    assert ht.slots < expanded_slots, "Error: Таблиця не зменшилась після масового видалення"
    assert ht.slots >= 10, "Error: Таблиця стала меншою за базовий розмір (10)"

    assert ht.get("apple") == 999, "Error: Дані 'apple' зламались після ресайзів"
    assert ht.get(10) == "B", "Error: Дані '10' зламались після ресайзів"

    print("Всі тести успішно пройдені!")