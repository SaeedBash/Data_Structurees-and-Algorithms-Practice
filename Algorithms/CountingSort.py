import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')


def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    
    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        index = count[num - min_val] - 1
        sorted_arr[index] = num
        count[num - min_val] -= 1

    return sorted_arr


clear_screen()

test = [1, 5, 6, 0, -4, 4, 12, 200, 12]
print(test)
counting_sort(test)
print(test)