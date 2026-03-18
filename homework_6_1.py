import copy


class Patient:
    DIAGNOSIS_PRIORITY = {
        'вивих гомілки': 1,
        'грип': 1,
        'підозра на апендицит': 2,
        'перелом': 3,
        'проблеми з диханням': 4,
        'зупинка серця': 4
    }

    def __init__(self, name: str, age: int, diagnosis: str):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.priority_level = self.DIAGNOSIS_PRIORITY.get(diagnosis.lower(), 1)

    def __lt__(self, other):
        if self.priority_level == other.priority_level:
            return self.age > other.age
        return self.priority_level < other.priority_level

    def __repr__(self):
        return f"[{self.priority_level}] {self.name} ({self.age}р.) - {self.diagnosis}"


class BinaryMaxPQ:
    def __init__(self):
        self._elements = [None]
        self._capacity = 0

    def __str__(self):
        array_copy = copy.deepcopy(self._elements[1:])
        array_copy.sort(reverse=True)
        return "\n".join(f"  {i}. {p}" for i, p in enumerate(array_copy, 1))

    def _swim(self, k):
        while k > 1 and self._less(k // 2, k):
            self._exch(k, k // 2)
            k = k // 2

    def insert(self, value):
        self._elements.append(value)
        self._capacity += 1
        self._swim(self._capacity)

    def _sink(self, k):
        while 2 * k <= self._capacity:
            j = 2 * k
            if j < self._capacity and self._less(j, j + 1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def del_max(self):
        if self._capacity == 0:
            return None
        max_el = self._elements[1]
        self._exch(1, self._capacity)
        self._capacity -= 1
        self._sink(1)
        del self._elements[-1]
        return max_el

    def _exch(self, k, j):
        self._elements[k], self._elements[j] = self._elements[j], self._elements[k]

    def _less(self, i, j):
        return self._elements[i] < self._elements[j]


class EmergencyRoom:
    def __init__(self):
        self.queue = BinaryMaxPQ()

    def register_patient(self, name: str, age: int, diagnosis: str):
        patient = Patient(name, age, diagnosis)
        self.queue.insert(patient)
        print(f"Зареєстровано: {patient}")

    def next_patient(self):
        patient = self.queue.del_max()
        if patient:
            print(f"Лікар приймає: {patient}")
        else:
            print("Черга порожня.")
        return patient

    def display_queue(self):
        if self.queue._capacity == 0:
            print("\nПоточна черга: порожня")
        else:
            print("\nПоточна черга:")
            print(self.queue)


if __name__ == "__main__":
    er = EmergencyRoom()

    er.register_patient("Ганна", 37, "грип")
    er.register_patient("Сергій", 58, "підозра на апендицит")
    er.register_patient("Іван", 29, "проблеми з диханням")
    er.register_patient("Аліса", 17, "перелом")
    er.register_patient("Сергій", 48, "підозра на апендицит")
    er.register_patient("Іван", 19, "проблеми з диханням")
    er.register_patient("Аліса", 27, "перелом")

    er.display_queue()

    er.next_patient()
    er.next_patient()
    er.next_patient()
    er.next_patient()
    er.next_patient()
