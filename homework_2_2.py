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
        output.append(node.data)
        node = node.next

    print(output)

if __name__ == "__main__":
    linked_list(parse("1 -> 2 -> None"))