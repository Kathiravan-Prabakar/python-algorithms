def quick_sort(arr: list) -> list:
    arrlen = len(arr)
    if arrlen <= 1:
        return arr
    else:
        top = arr.pop()
        gr8, small = [], []
        for i in arr:
            if i > top:
                gr8.append(i)
            else:
                small.append(i)
    return quick_sort(small) + [top] + quick_sort(gr8)

tosort = [45, 67, 21, 1]
print(quick_sort(tosort))