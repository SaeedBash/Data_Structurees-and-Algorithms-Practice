import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_R(arr, n=None):
    if n == None:
        n = len(arr)
    
    if n == 1:
        return arr

    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    
    if not swapped:
        return arr

    return bubble_sort_R(arr, n - 1)


clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
sorted = bubble_sort(test)
print(sorted)
r_sorted = bubble_sort_R(test)
print(r_sorted)