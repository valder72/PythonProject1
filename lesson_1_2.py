class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self._size = 0

    def insert_to_start(self, data):
        """
        add a node at begin of linked-list
        :param data:
        :return:
        """
        new_first_node = Node(data)
        if self.head_node is None:
            self.head_node = new_first_node
            self.tail_node = new_first_node
        else:
            new_first_node.next = self.head_node
            self.head_node.prev = new_first_node
            self.head_node = new_first_node
        self._size += 1

    def insert_to_end(self, data):
        """
        add a node at the end of linked-list
        :param data:
        :return:
        """
        new_last_node = Node(data)
        if self.tail_node is None:
            self.head_node = new_last_node
            self.tail_node = new_last_node
        else:
            new_last_node.prev = self.tail_node
            self.tail_node.next = new_last_node
            self.tail_node = new_last_node
        self._size += 1

    def remove_head(self):
        """
        remove first node of linked list
        :return:
        """
        if self.head_node is None:
            return None
        first_node_data = self.head_node.data
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
            self._size -= 1
            return first_node_data
        self.head_node = self.head_node.next
        self.head_node.prev.next = None
        self.head_node.prev = None
        self._size -= 1
        return first_node_data

    def remove_tail(self):
        """
        remove last node of linked list
        :return:
        """
        if self.tail_node is None:
            return None
        last_node_data = self.tail_node.data
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
            self._size -= 1
            return last_node_data
        self.tail_node = self.tail_node.prev
        self.tail_node.next.prev = None
        self.tail_node.next = None
        self._size -= 1
        return last_node_data

    def size(self) -> int:
        """
        return size of linked list
        :return: int
        """
        return self._size

    def show(self):
        """
        print linked list
        :return:
        """
        output = []
        current_node = self.head_node
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)


class Stack:
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def push(self, data):
        return self.doubly_linked_list.insert_to_end(data)

    def pop(self):
        return self.doubly_linked_list.remove_tail()

    def empty(self):
        return self.doubly_linked_list.size() == 0

    def top(self):
        if self.doubly_linked_list.tail_node is None:
            return None
        return self.doubly_linked_list.tail_node.data

    def size(self):
        return self.doubly_linked_list.size()

    def __iter__(self):
        current_stack_node = self.doubly_linked_list.tail_node
        while current_stack_node is not None:
            yield current_stack_node.data
            current_stack_node = current_stack_node.prev

class Queue:
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def is_empty(self):
        return self.doubly_linked_list.size() == 0

    def size(self):
        return self.doubly_linked_list.size()

    def enqueue(self, data):
        return self.doubly_linked_list.insert_to_end(data)

    def dequeue(self):
        return self.doubly_linked_list.remove_head()

    def __iter__(self):
        current_queue_node = self.doubly_linked_list.head_node
        while current_queue_node is not None:
            yield current_queue_node.data
            current_queue_node = current_queue_node.next

if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_to_start('c')
    doubly_linked_list.insert_to_end('abc')
    doubly_linked_list.insert_to_start(32)
    doubly_linked_list.insert_to_start(['a', '32', 32])
    doubly_linked_list.insert_to_start((['a'], 12))
    doubly_linked_list.show()
    print(doubly_linked_list.size())
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_head()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()

    stack = Stack()
    stack.push('a')
    stack.push('3')
    stack.push([1, 2, 3])
    for s in stack:
        print(s)
    print(stack.top())
    print(stack.size())
    stack.pop()
    stack.pop()
    print(stack.empty())
    stack.pop()
    print(stack.empty())

    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('3')
    queue.enqueue([1, 2, 3])
    for q in queue:
        print(q)
    print(queue.size())
    queue.dequeue()
    queue.dequeue()
    print(queue.is_empty())
    queue.dequeue()
    print(queue.is_empty())