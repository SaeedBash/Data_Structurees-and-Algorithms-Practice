import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class MinHeap:
    def __init__(self, input_list=None):
        if input_list:
            self._build_heap(input_list)
        else:
            self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return index * 2 + 1
    
    def get_right_child_index(self, index):
        return index * 2 + 2
    
    def has_parent(self, index):
        return index > 0
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    
    def delete(self, index):
        self._swap(index, len(self.heap) - 1)
        value = self.heap.pop()
        self._heapify_down(index)

    def extract(self, index):
        if index < 0 or index >= len(self.heap):
            return None
        self._swap(index, len(self.heap) - 1)
        value = self.heap.pop()
        if index < len(self.heap):
            self._heapify_down(index)
            self._heapify_down(index)
        return value
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        return self.extract(0)

    def peek_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while self.has_left_child(index):
            smallest_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.heap[self.get_right_child_index(index)] < self.heap[smallest_child_index]:
                smallest_child_index = self.get_right_child_index(index)

            if self.heap[index] <= self.heap[smallest_child_index]:
                break
            
            self._swap(index, smallest_child_index)
            index = smallest_child_index

    def is_empty(self):
        return len(self.heap) == 0
    
    def display(self, index, indent=0):
        if index < len(self.heap) - 1:
            self.display(self.get_right_child_index(index), indent + 4)
            
            print(" " * indent + f"-> {self.heap[index]}")
            
            self.display(self.get_left_child_index(index), indent + 4)

    def get_height(self):
        index = 0
        height = 1
        while self.has_left_child(index):
            index = self.get_left_child_index(index)
            height += 1
        return height
    
    def change_key(self, index, new_val):
        if not (0 <= index < len(self.heap)):
            raise IndexError("Heap index out of range")
        elif new_val == self.heap[index]:
            return
        elif new_val < self.heap[index]:
            self._decrease_key(index, new_val)
        elif new_val > self.heap[index]:
            self._increase_key(index, new_val)

    def _decrease_key(self, index, new_val):
        self.heap[index] = new_val
        self._heapify_up(index)

    def _increase_key(self, index, new_value):
        self.heap[index] = new_value
        self._heapify_down(index)

    def _build_heap(self, input_list):
        self.heap = input_list[:]
        n = len(self.heap)
    
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def add_list(self, new_elements):
        self.heap.extend(new_elements)

        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)


clear_screen()

#tests

data = [3, 4, 1, 7, 20, -1, 12, 14, 15, 16, 17, 18, 19, 200, 300, 400, 500, 600, 1000, 2000, 3000, 4000, 5000, 7000]
h = MinHeap(data)

print(h.heap)

min = h.extract_min()
print(min)
print(h.heap)
h.delete(1)
print(h.extract(1))
print()
h.display(0)