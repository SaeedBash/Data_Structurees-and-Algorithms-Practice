import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def selection_sort_R(arr, n=None):
    if n == None:
        n = 0
    
    if n >= len(arr) - 1:
        return arr
    
    min_idx = n
    for i in range(n + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i

    if min_idx != n:
        arr[n], arr[min_idx] = arr[min_idx], arr[n]

    return selection_sort_R(arr, n+1)
    
    
    


clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
sorted = selection_sort(test)
print(sorted)
r_sorted = selection_sort_R(test)
print(r_sorted)