import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
sorted = merge_sort(test)
print(sorted)