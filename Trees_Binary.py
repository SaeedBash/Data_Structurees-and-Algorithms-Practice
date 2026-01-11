import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child_left(self, child_node):
        child_node.parent = self
        self.left = child_node

    def add_child_right(self, child_node):
        child_node.parent = self
        self.right = child_node

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level=0):
        prefix = " " * (level * 4) + "|__" if level > 0 else ""
        print(f"{prefix}{self.data}")
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)

    def traverse_inorder(self):
        """Yields nodes in order: Left -> Root -> Right."""
        if self.left:
            yield from self.left.traverse_inorder()
        yield self.data
        if self.right:
            yield from self.right.traverse_inorder()

    def traverse_preorder(self):
        """Yields nodes in order: Root -> Left -> Right."""
        yield self.data
        if self.left:
            yield from self.left.traverse_preorder()
        if self.right:
            yield from self.right.traverse_preorder()

    def traverse_postorder(self):
        """Yields nodes in order: Left -> Right -> Root."""
        if self.left:
            yield from self.left.traverse_postorder()
        if self.right:
            yield from self.right.traverse_postorder()
        yield self.data

clear_screen()

#tests:

root = BTreeNode("Root")
root.left = BTreeNode("Left Child")
root.right = BTreeNode("Right Child")

root.left.left = BTreeNode("Left-Left")
root.left.right = BTreeNode("Left-Right")

root.right.left = BTreeNode("Right-Left")
root.right.right = BTreeNode("Right-Right")

print("Tree Structure:")
root.print_tree()

print("\nin-order traversal:")
for node in root.traverse_inorder():
    print(node)

print("\npre-order traversal:")
for node in root.traverse_preorder():
    print(node)

print("\npost-order traversal:")
for node in root.traverse_postorder():
    print(node)