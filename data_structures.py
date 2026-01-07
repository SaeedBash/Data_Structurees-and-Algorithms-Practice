from collections import deque

# =====================
# Stack (LIFO)
# =====================
class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        if self.is_empty():
            return "Empty Stack"
        string = "####TOP####\n"
        for item in reversed(self.stack):
            string += str(item) + "\n"
        string += "###Bottom###"
        return string

    def push(self, item):
        self.stack.append(item)

    def push_multi(self, iterable):
        for item in iterable:
            self.push(item)  # preserves order

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def pop_all(self):
        items = self.stack.copy()
        self.stack.clear()
        return items

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# =====================
# Queue (FIFO)
# =====================
class Queue:
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        if self.is_empty():
            return "Empty Queue"
        return "[End of Queue] " + " -> ".join(str(x) for x in self.queue) + " [Start of Queue]"

    def push(self, item):
        self.queue.appendleft(item)  # Append to the “end” for FIFO

    def push_multi(self, iterable):
        for item in iterable:
            self.push(item)

    def peek(self, index=0):
        """0-based indexing: peek(0) returns first element (front of queue)"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        if index < 0 or index >= len(self.queue):
            raise IndexError(f"Queue index out of range, size={len(self.queue)}")
        return self.queue[-1 - index]

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty queue")
        return self.queue.pop()

    def pop_all(self):
        items = list(self.queue)
        self.queue.clear()
        return items

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


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
