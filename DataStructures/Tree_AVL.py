import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def left_rotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case (Right Rotation)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case (Left Rotation)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case (Left then Right Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case (Right then Left Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def pre_order_traversal(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def display(self, root, indent=0):
        if root:
            self.display(root.right, indent + 4)
            
            print(" " * indent + f"-> {root.key}")
            
            self.display(root.left, indent + 4)

clear_screen()

#tests 

myTree = AVLTree()
root = None
elements = [1, 2, 3, 10, 20, 30, 40, 50, 25, 70, 100, 1000, 2000, 3000, 5000, 7000]

for element in elements:
    root = myTree.insert(root, element)

print("Pre-order traversal of the constructed AVL tree is:")
myTree.pre_order_traversal(root)
print()
myTree.display(root)