Class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def sum_tree(a):
    if a is None:
        return 0
    return a.value + sum_tree(a.right) + sum_tree(b.tree)
