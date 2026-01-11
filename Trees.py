import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level=0):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix}{self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()

    def traverse_depth_first(self):
        yield self
        for child in self.children:
            yield from child.traverse_depth_first()

    
clear_screen()

#tests:

root = TreeNode("Electronics")

laptop = TreeNode("Laptops")
laptop.add_child(TreeNode("MacBook"))
laptop.add_child(TreeNode("Surface"))

phone = TreeNode("Phones")
phone.add_child(TreeNode("iPhone"))
phone.add_child(TreeNode("Android"))

root.add_child(laptop)
root.add_child(phone)

root.print_tree()