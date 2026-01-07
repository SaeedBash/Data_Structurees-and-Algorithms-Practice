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