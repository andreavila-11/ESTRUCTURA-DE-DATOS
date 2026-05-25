# Lista original
lista_original = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]


# BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# SELECTION SORT       
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr


# MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# QUICK SORT
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


import random

# QUICK SORT RANDOM
def partition_random(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quick_sort_random(arr, low, pi - 1)
        quick_sort_random(arr, pi + 1, high)
    return arr

# COUNTING SORT
def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr



# =========================
# EJECUCIÓN 
# =========================

#  BUBBLE SORT
listaN = lista_original.copy()                                                                                                                                                                                                                                                                                                      
print("Bubble Sort:", bubble_sort(listaN))
print()

# SELECTION SORT
listaN = lista_original.copy()
print("Selection Sort:", selection_sort(listaN))
print()

# INSERTION SORT
listaN = lista_original.copy()
print("Insertion Sort:", insertion_sort(listaN))
print()

# MERGE SORT
listaN = lista_original.copy()
print("Merge Sort:", merge_sort(listaN))
print()

# QUICK SORT
listaN = lista_original.copy()
print("Quick Sort:", quick_sort(listaN, 0, len(listaN) - 1))
print()

# QUICK SORT RANDOM
listaN = lista_original.copy()
print("Quick Sort Random:", quick_sort_random(listaN, 0, len(listaN) - 1))
print()

# COUNTING SORT
listaN = lista_original.copy()
print("Counting Sort:", counting_sort(listaN))
