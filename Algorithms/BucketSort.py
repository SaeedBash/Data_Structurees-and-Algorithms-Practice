import os
from math import floor
import SelectionSort as ss

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

def bucket_sort(arr):
    n = len(arr)
    if n <= 1: return arr
    
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val
    
    if range_size == 0: return arr

    buckets = [[] for _ in range(n)]

    for num in arr:
        # Improved indexing to prevent IndexError on max_val
        index = int((num - min_val) * (n - 1) / range_size)
        buckets[index].append(num)
    print(buckets)
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = ss.selection_sort(bucket)
        sorted_arr.extend(sorted_bucket)
    return sorted_arr

clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
sorted = bucket_sort(test)
print(sorted)