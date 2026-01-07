# To Implement some Data Structures from scratch; To deepen understanding and practice programming

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
        temp = self.stack[-1]
        self.stack = self.stack[:-1]
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


#Stack Tests

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

