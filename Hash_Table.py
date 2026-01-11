import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class Hash_Table:

    def __init__(self, bucket):
        self.__bucket = bucket
        self.__table = [[] for _ in range(bucket)]

    def hashFucntion(self, key):
        return (key % self.__bucket)
    
    def insertItem(self, key):
        index = self.hashFucntion(key)
        self.__table[index].append(key)

    def deleteItem(self, key):
        index = self.hashFucntion(key)
        if key not in self.__table[index]:
            return
        self.__table[index].remove(key)

    def displayHash(self):
        print("Index\tKeys")
        for i in range(self.__bucket):
            print("[%d]" % i, end='')
            for x in self.__table[i]:
                print(" --> %d" % x, end='')
            print()
        print()

clear_screen()

#Tests

keys = [15, 11, 27, 8, 12]

h = Hash_Table(10)

for k in keys:
    h.insertItem(k)

h.displayHash()

h.deleteItem(12)

h.displayHash()

