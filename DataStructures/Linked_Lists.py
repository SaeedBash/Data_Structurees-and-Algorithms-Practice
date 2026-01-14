import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

# =====================
# Singly Linked List
# =====================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return " -> ".join(str(node) for node in self)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    # Add node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Insert at a specific index (0-based)
    def insert(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError(f"Index out of range: 0-{self.length}")

        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def contains(self, value):
        return any(node == value for node in self)

    def find(self, value):
        index = 0
        for node in self:
            if node == value:
                return index
            index += 1
        return -1  # not found

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if self.head == self.tail:
            self.clear()
            return
        self.head = self.head.next
        self.length -= 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if self.head == self.tail:
            self.clear()
            return

        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current
        self.length -= 1

    def remove(self, index):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.remove_first()
            return
        if index == self.length - 1:
            self.remove_last()
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1

    def find_del(self, value):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.value == value:
            self.remove_first()
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                self.length -= 1
                return
            prev, curr = curr, curr.next

        raise ValueError(f"Value {value} not found in list")

    def get_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.head.value

    def get_last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.tail.value

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def to_list(self):
        return list(self)

    def reverse(self):
        if self.length <= 1:
            return

        prev = None
        curr = self.head
        self.tail = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

# =====================
# Doubly Linked List
# =====================

class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.middle = self.length // 2

    def __repr__(self):
        return "HEAD <-> " + " <-> ".join(str(node) for node in self) + " <-> TAIL"

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    # Add node at the beginning
    def prepend(self, data):
        new_node = DNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        self.middle = self.length // 2

    # Add node at the end
    def append(self, data):
        new_node = DNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        self.middle = self.length // 2

    # Insert at a specific index (0-based)
    def insert(self, data, index):
        if index < 0 or index > self.length:
            raise IndexError(f"Index out of range: 0-{self.length}")

        if index == 0:
            self.prepend(data)
            return
        if index == self.length:
            self.append(data)
            return

        new_node = DNode(data)
        if index < self.middle:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        else: 
            current = self.tail
            for _ in range(self.length - index):
                current = current.prev
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
        
        self.length += 1
        self.middle = self.length // 2

    def contains(self, value):
        return any(node == value for node in self)

    def find(self, value):
        index = 0
        for node in self:
            if node == value:
                return index
            index += 1
        return -1  # not found

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if self.head == self.tail:
            self.clear()
            return
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        self.middle = self.length // 2

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if self.head == self.tail:
            self.clear()
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        self.middle = self.length // 2

    def remove(self, index):
        if self.is_empty():
            raise IndexError("Remove from empty list")
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.remove_first()
            return
        if index == self.length - 1:
            self.remove_last()
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        to_remove = current.next
        current.next = to_remove.next
        if to_remove.next:
            to_remove.next.prev = current
        self.length -= 1
        self.middle = self.length // 2

    def find_del(self, value):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.value == value:
            self.remove_first()
            return

        curr = self.head.next
        while curr:
            if curr.value == value:
                if curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                else:    
                    curr.next.prev = curr.prev
                
                curr.prev.next = curr.next
                
                self.length -= 1
                self.middle = self.length // 2
                return
            curr = curr.next

        raise ValueError(f"Value {value} not found in list")

    def get_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.head.value

    def get_last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.tail.value

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        
        if index < self.middle:    
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value
        else:
            current = self.tail
            for _ in range(self.length-index-1):
                current = current.prev
            return current.value

    def clear(self):
        self.head = self.tail = None
        self.length = self.middle = 0

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def to_list(self):
        lists = []
        for node in self:
            lists.append(node)
        return lists

    def reverse(self):
        if self.length <= 1:
            return

        curr = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
        
        self.head, self.tail = self.tail, self.head
        

clear_screen()

#Test DL:

list = ["potato", "tomato", "banana", "eggplant"]
DL = DoublyLinkedList()
for item in list:
    DL.append(item)
DL.prepend("nuts")
DL.insert("strawberry", 4)
print(DL)
# print(DL.contains("nuts"), DL.contains("eggplant"))
# print(DL.find("nuts"), DL.find("NUTS"))
# DL.remove_first()
# DL.remove_last()
# DL.remove(2)
# DL.find_del("tomato")
# print(DL.get_first(), DL.get_last())
# for i in range(DL.length):
#    print(DL.get(i))
# print(DL.is_empty())
# DL.clear()
# print(DL.is_empty())
# list = DL.to_list()
# print(list)
DL.reverse()
print(DL)
