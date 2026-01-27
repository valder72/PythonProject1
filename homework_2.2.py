class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def parse(string):
    if string == "None":
        return None

    parts = string.split(" -> ", 1)
    data = int(parts[0])
    rest = parts[1]

    return Node(data, parse(rest))

def linked_list(node):
    output = []
    while node:
        output.append(str(node.data))
        node = node.next
    print(" -> ".join(output) + " -> None")

if __name__ == "__main__":
