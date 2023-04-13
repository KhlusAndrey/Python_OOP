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


if __name__ == "__main__":
    # print(quick_sort(arr))
    print(merge_sort(arr))
