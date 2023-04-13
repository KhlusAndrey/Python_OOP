import timeit
from functools import partial

# Быстрая сортировка (Quick sort) Horan (1960):

arr: list = [9, 8, 6, 5, 4, 3, 2, 1, 4, 2, 5, 6, 7, 8, 9, 5, 4, 3, 4, 6, 7, 9]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка слиянием (Merge sort):
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# Пирамидальная сортировка (Heap sort):
def heap_sort(arr):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for start in range((len(arr)-2)//2, -1, -1):
        sift_down(start, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(0, end - 1)
    return arr


# Сортировка вставками (Insertion sort):

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

# Сортировка выбором (Selection sort):

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Сортировка пузырьком (Bubble sort):
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    quick = min(timeit.repeat(partial(quick_sort, arr), number=10000))
    print(f'Min time for Quick sort: {quick}')
    merge = min(timeit.repeat(partial(merge_sort, arr), number=10000))
    print(f'Min time for Merge sort: {merge}')
    heap = min(timeit.repeat(partial(heap_sort, arr), number=10000))
    print(f'Min time for Heap sort: {heap}')
    insertion = min(timeit.repeat(partial(insertion_sort, arr), number=10000))
    print(f'Min time for Insertion sort: {insertion}')
    selection = min(timeit.repeat(partial(selection_sort, arr), number=10000))
    print(f'Min time for Selection sort: {selection}')
    bubble = min(timeit.repeat(partial(bubble_sort, arr), number=10000))
    print(f'Min time for Bubble sort: {bubble}')

    # print(quick_sort(arr))
    # print(merge_sort(arr))
    # print(heap_sort(arr))
    # print(insertion_sort(arr))
    # print(selection_sort(arr))
    # print(bubble_sort(arr))
