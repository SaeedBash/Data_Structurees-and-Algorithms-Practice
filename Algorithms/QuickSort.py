import os
from random import randint

# FIRST TRY

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     # change the pivot_idx definetion to change the method (first, last, median, random)
#     pivot_idx = randint(0, len(arr)-1)
#     pivot_val = arr[pivot_idx]

#     left, right = partition(arr, pivot_idx)

#     left = quick_sort(left)
#     right = quick_sort(right)
    
#     arr = left + [pivot_val] + right

#     return arr

# PART OF THE 1ST TRY
# def partition(arr, pivot_idx):
#     left = []
#     right = []
#     pivot_val = arr[pivot_idx]

#     for i in range(len(arr)):
#         if i == pivot_idx:
#             continue
#         elif arr[i] <= pivot_val:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])

#     return left, right

# VERY CLEAN VERSION
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[randint(0, len(arr)-1)]

    left  = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
sorted = quick_sort(test)
print(sorted)