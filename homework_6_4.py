class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, val, priority):
        self.queue.append((priority, val))

    def remove_max(self):
        max_idx = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[max_idx][0]:
                max_idx = i

        val = self.queue[max_idx][1]
        while max_idx < len(self.queue) - 1:
            self.queue[max_idx] = self.queue[max_idx + 1]
            max_idx += 1
        self.queue.pop()
        return val


if __name__ == "__main__":
    # Example usage
    pq = PriorityQueue()
    pq.insert("Task 1", 1)
    pq.insert("Task 4", 4)
    pq.insert("Task 2", 2)
    pq.insert("Task 3", 3)
    print(pq.remove_max())
    print(pq.remove_max())
    print(pq.remove_max())
    print(pq.remove_max())
