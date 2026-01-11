import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class HNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def __hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self.__hash(key)
        if self.table[index] is None: #if not (index in self.table): DOESNT WORK
            self.table[index] = HNode(key, value)
            self.size += 1

        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value == value
                    return
                current = current.next
            new_Node = HNode(key, value)
            new_Node.next = self.table[index]
            self.table[index] = new_Node
            self.size += 1

    def search(self, key):
        index = self.__hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)
                
    def remove(self, key):
        index = self.__hash(key)

        previous = None
        current = self.table[index]
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size += 1
                return
            previous = current
            current = current.next
        raise KeyError
    
    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)
    
    def __len__(self):
        return self.size
    
    # def __contains__(self, key):
    #     try:
    #         self.search(key)
    #         return True
    #     except KeyError:
    #         return False
clear_screen

#tests:

ht = HashTable(5)

stuff = [("nuts", 3), ("strawberry", 5), ("potato", 3)]
for item, number in stuff:
    ht.insert(item, number)

print(len(ht))
print(ht)

print(ht.search("nuts"))

ht.insert("nuts", 55)

ht.remove("strawberry")

print(len(ht))
print(ht)