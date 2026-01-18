import os
from math import sqrt
from MergeSort import merge_sort


def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

def linear_search(data, target):
    arr_data = merge_sort(data)
    for i in range(len(arr_data)):
        if arr_data[i] == target:
            return i
    return -1 

def binary_search(data, target):
    
    arr_data = merge_sort(data)
    left = 0
    right = len(arr_data) - 1

    while left < right:
        mid = (right - left) // 2
        if arr_data[mid] == target:
            return mid
        elif arr_data[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# COPIED target seach
def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
            
    return -1

def f(x):
    return (x - 2)**2 + 3

def nf(x):
    return -1 * ((x - 2)**2 + 3) 

def ternary_search_min(f, l, r, eps=1e-9):
    while (r - l) > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        
        if f(m1) < f(m2):
            # Minimum is in [l, m2]
            r = m2
        else:
            # Minimum is in [m1, r]
            l = m1
            
    return (l + r) / 2

def ternary_seach_max(f, l, r, eps=1e-9):
    while (r - l) > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3

        if f(m1) < f(m2):
            l = m1
        else:
            r = m2
        
    return (l + r) / 2

def jump_search(data, target):
    arr_data = merge_sort(data)
    n = len(data)
    step = int(sqrt(n))
               
    while data[min(step, n) - 1] < target:
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1

    while data[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if data[prev] == target:
        return prev

def binary_search_range(data, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(data, target):
    n = len(data)
    if n == 0:
        return -1
    
    arr_data = merge_sort(data)

    if arr_data[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr_data[i] <= target:
        i *= 2
    
    # Call binary search for the identified range
    return binary_search_range(arr_data, target, i // 2, min(i, n - 1))

clear_screen()

# Tests:

my_list = [4, 2, 7, 5, 12, 54, 21, 64, 12, 32]
target_value = 12

result_index = linear_search(my_list, target_value)
result_index = binary_search(my_list, target_value)
result_index = ternary_search(my_list, target_value)
result_index = jump_search(my_list, target_value)
result_index = exponential_search(my_list, target_value)

if result_index != -1:
    print(f"Element {target_value} found at index: {result_index}")
else:
    print(f"Element {target_value} not found in the list.")

target_value_not_found = 100
result_index_not_found = linear_search(my_list, target_value_not_found)
result_index_not_found = binary_search(my_list, target_value_not_found)
result_index_not_found = ternary_search(my_list, target_value_not_found)
result_index_not_found = jump_search(my_list, target_value_not_found)
result_index_not_found = exponential_search(my_list, target_value_not_found)

if result_index_not_found != -1:
    print(f"Element {target_value_not_found} found at index: {result_index_not_found}")
else:
    print(f"Element {target_value_not_found} not found in the list.")

# min = ternary_search_min(f, -100, 100)
# print(f"Minimum found at x = {min}")

# max = ternary_seach_max(nf, -100, 100)
# print(f"Maximum found at x = {max}")