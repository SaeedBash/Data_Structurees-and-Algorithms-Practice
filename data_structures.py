# To Implement some Data Structures from scratch; To deepen understanding and practice programming

from collections import deque

class Stack:

    def __init__(self):
        self.stack = []

    def __repr__(self):

        if self.isEmpty() == True:
            return "Empty Stack"

        string = "####TOP####\n"
        for i in range(self.size()):
            string = string + str(self.stack[-i-1]) + "\n" 
        string = string + "###Bottom###"

        return string

    def push(self, item):
        self.stack.append(item)

    def push_multi(self, iterable):

        for item in iterable:
            self.push(item)
            
        
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        temp = self.stack[0]
        self.stack = self.stack[1:]
        return temp
    
    def pop_all(self):
        temp = self.stack
        self.stack = []
        return temp

    def isEmpty(self):
        if self.stack == []: return True
        return False
    
    def size(self):
        return len(self.stack)

class Queue:

    def __init__(self):
        self.queue = deque()

    def __repr__(self):

        if self.isEmpty() == True:
            return "Empty queue"

        string = "[End of queue]     "
        for i in range(self.size()):
            string = string + str(self.queue[i]) + "     " 
        string = string + "[Start of queue]"

        return string

    def push(self, item):
        self.queue.appendleft(item)

    def push_multi(self, iterable):

        for item in iterable:
            self.push(item)
            
        
    def peek(self, i=1):
        
        if self.isEmpty() == True:
            return "queue is empty"
        
        try:
            return self.queue[-i]
        except IndexError:
            return f"Last position in queue is #{self.size()}"
            
    
    def pop(self):
        return self.queue.pop()
    
    def pop_all(self):
        temp = self.queue
        self.queue = []
        return temp

    def isEmpty(self):
        if self.size() == 0: return True
        return False
    
    def size(self):
        return len(self.queue)

# for Singly Linked Lists
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# Singly(?) Linked List
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        # """Helper method to represent the list as a string for easy printing."""
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self, new_node):
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def append(self, new_node):

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def insert(self, new_node, index):
        
        if index < 1:
            print("Insert a valid index.\nInsertion aborted.")
            return

        elif index == 1:
            print("Please use the \"prepend\" method to attach a node to the head of the linked list.\nInsertion aborted.")
            return
        
        elif index == self.length:
            print("Please use the \"append\" method to attach a node to the tail of the linked list.\nInsertion aborted.")
        
        elif index > self.length:
            print("Index is bigger than the linked list's length!\nInsertion aborted.")
            return

        temp = self.head
        for i in range(1, index-1):
            temp = temp.next
        temp2 = temp.next
        
        temp.next = new_node
        new_node.next = temp2

        self.length += 1

    def contains(self, value):
        
        current_node = self.head
        
        while current_node:
            if current_node.value == value: return True
            current_node = current_node.next
        
        return False
    
    def find(self, value):
        
        i = 1
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return f"Found at index #{i}"
            current_node = current_node.next
            i += 1
        
        return "Value Not Found"

    def remove_first(self):
        temp = self.head.next
        self.head = temp
        self.length -= 1

    def remove_last(self):
        temp = self.head
        for i in range(self.length-2):
            temp = temp.next
        
        temp.next = None
        self.tail = temp
        self.length -= 1

    def remove(self, index):
        
        if index < 1:
            print("Insert a valid index.\nRemoving aborted.")
            return

        elif index == 1:
            print("Please use the \"remove_first\" method to remove the head of the linked list.\nRemoving aborted.")
            return
        
        # elif index == self.length:
            # print("Please use the \"remove_last\" method to remove the tail of the linked list.\nRemoving aborted.")
        
        elif index > self.length:
            print("Index is bigger than the linked list's length!\nInsertion aborted.")
            return
        
        i = 1
        current_node = self.head

        while i < (index-1):
            current_node = current_node.next
            i += 1
        
        temp = current_node
        target_node = current_node.next
        temp.next = target_node.next

        self.length -= 1

    def find_del(self, value):

        current_node = self.head

        if current_node.value == value:
            self.remove_first()
            return

        found = False

        while current_node:
            if current_node.value == value:
                found = True
                break
            previous_node = current_node
            current_node = current_node.next

        if found:
            previous_node.next = current_node.next
            self.length -= 1
        
        else:
            print("Value Not Found")
        
        

    def traverse(self):
        
        current_node = self.head
        
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        
        print("None")

    def getFirst(self):
        return self.head.value

    def getLast(self):
        return self.tail.value

    def get(self, index):
        
        if index < 1:
            print("Insert a valid index.")
            return
        
        elif index > self.length:
            print("Index is bigger than the linked list's length!")
            return
        
        i = 1
        current_node = self.head

        while i < (index):
            current_node = current_node.next
            i += 1
        
        return current_node.value

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        if self.head == None: return True
        return False

    def size(self):
        return self.length
    
    def toArray(self):
        pass

    def reverse(self):
        pass


    
# Stack Tests:

    # new = Stack()

    # print(new.isEmpty())
    # print(new)

    # new.push("Potato")
    # print(new.isEmpty())
    # print(new.size())
    # print(new)

    # print(new.peek())
    # print(new.pop())
    # print(new.size())
    
    # list = ["Potato", "Carrot", "Tomato"]
    # new.push_multi(list)
    # print(new.stack)
    # print(new)
    
    # new.pop_all()
    # print(new)

# Queue Tests:

    # new = Queue()

    # print(new.isEmpty())
    # print(new)

    # new.push("Potato")
    # print(new.isEmpty())
    # print(new.size())
    # print(new)

    # print(new.peek())
    # print(new.peek(1))
    # print(new.peek(2))
    # print(new.pop())
    # print(new.size())

    # list = ["Potato", "Carrot", "Tomato"]
    # new.push_multi(list)
    # print(new.queue)
    # print(new)
    # print(new.pop())
    # new.push("Banana")
    # print(new)
    # print(new.isEmpty())
    # new.pop_all()
    # print(new.isEmpty())
    # print(new.size())
    # print(new)

# LinkedList Tests:

LL = LinkedList()
#print(LL.isEmpty())

node_list = [Node("Potato"), Node("Tomato"), Node("Banana"), Node("Lemon")]
for node in node_list:
    LL.append(node)
LL.prepend(Node("Nuts"))

# print(f"First: {LL.getFirst()}\nLast: {LL.getLast()}")

LL.insert(Node("TEST"), 3)
# LL.traverse()

# LL.remove_first()
# LL.traverse()
# LL.remove_last()
# LL.traverse()
# print(f"Length: {LL.size()}")
# LL.remove(2)
# print(f"Length: {LL.size()}")
# LL.traverse()

# print(f"Length: {LL.size()}")

# print(f"{LL.contains("TEST")} {LL.contains("IDK")}")

# print(f"{LL.find('nuts')}   {LL.find('Nuts')}")

LL.find_del("TEST")
LL.traverse()

# print(LL.isEmpty())

# print(LL.get(6))

# LL.clear()
# LL.traverse()