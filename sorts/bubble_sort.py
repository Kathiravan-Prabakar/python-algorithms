def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

tosort = [67, 49, 69, 88, 95, 74]
bubbleSort(tosort)
print("Sorted Array: ")
for i in range(len(tosort)):
    print(f"{tosort[i]}")