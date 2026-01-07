from collections import deque

# =====================
# Stack
# =====================
class Stack:

    def __init__(self):
        self.stack = []

    def __repr__(self):
        if self.isEmpty():
            return "Empty Stack"

        string = "####TOP####\n"
        for i in range(self.size()):
            string += str(self.stack[-i-1]) + "\n"
        string += "###Bottom###"
        return string

    def push(self, item):
        self.stack.append(item)

    def push_multi(self, iterable):
        for item in iterable:
            self.push(item)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return
        return self.stack.pop()   # FIXED (LIFO)

    def pop_all(self):
        temp = self.stack.copy()
        self.stack = []
        return temp

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


# =====================
# Queue
# =====================
class Queue:

    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        if self.isEmpty():
            return "Empty queue"

        string = "[End of queue]     "
        for i in range(self.size()):
            string += str(self.queue[i]) + "     "
        string += "[Start of queue]"
        return string

    def push(self, item):
        self.queue.appendleft(item)

    def push_multi(self, iterable):
        for item in iterable:
            self.push(item)

    def peek(self, i=1):
        if self.isEmpty():
            return "queue is empty"
        try:
            return self.queue[-i]
        except IndexError:
            return f"Last position in queue is #{self.size()}"

    def pop(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        return self.queue.pop()

    def pop_all(self):
        temp = list(self.queue)
        self.queue = deque()   # FIXED (type preserved)
        return temp

    def isEmpty(self):
        return self.size() == 0

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
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, data, index):
        if index < 1:
            print("Insert a valid index.\nInsertion aborted.")
            return

        if index == 1:
            self.prepend(data)        # FIXED
            return

        if index == self.length + 1:
            self.append(data)         # FIXED
            return

        if index > self.length + 1:
            print("Index is bigger than the linked list's length!\nInsertion aborted.")
            return

        new_node = Node(data)
        temp = self.head
        for _ in range(1, index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def find(self, value):
        index = 1
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove_first(self):
        if self.isEmpty():
            print("List is Empty!")
            return

        if self.head == self.tail:
            self.clear()
            return

        self.head = self.head.next
        self.length -= 1

    def remove_last(self):
        if self.isEmpty():
            print("List is Empty!")
            return

        if self.head == self.tail:
            self.clear()
            return

        temp = self.head
        for _ in range(self.length - 2):
            temp = temp.next

        temp.next = None
        self.tail = temp
        self.length -= 1

    def remove(self, index):
        if self.isEmpty():
            print("List is Empty!")
            return

        if self.head == self.tail:
            self.clear()
            return

        if index < 1:
            print("Insert a valid index.\nRemoving aborted.")
            return

        if index > self.length:
            print("Index is bigger than the linked list's length!\nRemoving aborted.")
            return

        if index == 1:
            self.remove_first()
            return

        current = self.head
        for _ in range(1, index - 1):
            current = current.next

        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self.length -= 1

    def find_del(self, value):
        if self.isEmpty():
            print("List is Empty!")
            return

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
            prev = curr
            curr = curr.next

        print("Value Not Found")

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def getFirst(self):
        if self.isEmpty():
            print("List is Empty!")
            return
        return self.head.value

    def getLast(self):
        if self.isEmpty():
            print("List is Empty!")
            return
        return self.tail.value

    def get(self, index):
        if self.isEmpty():
            print("List is Empty!")
            return

        if index < 1 or index > self.length:
            print("Invalid index!")
            return

        current = self.head
        for _ in range(1, index):
            current = current.next
        return current.value

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.length

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        if self.isEmpty() or self.head == self.tail:
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
