class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def convert_to_string(node: None) -> str:
    if not node:
        return "NULL"
    return f"{node.data} -> " + convert_to_string(node.next)

if __name__ == '__main__':
    print(convert_to_string(None))
    print(convert_to_string(Node(4, Node(5, Node(7)))))
    print(convert_to_string(Node("ala")))