from heapq import heapify

def heap_sort(arr: list) -> list:
    arrlen = len(arr)
    for i in range(arrlen//2-1, -1, -1):
        heapify(arr)
    for i in range(arrlen - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr)
    return arr

arr = [12, 34, 13, 15, 42, 5]
print(heap_sort(arr))