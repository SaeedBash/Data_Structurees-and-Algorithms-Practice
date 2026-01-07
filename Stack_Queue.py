from collections import deque
import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')


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

clear_screen()
