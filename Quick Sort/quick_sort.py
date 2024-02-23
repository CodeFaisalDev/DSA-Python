def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[-1]

        less_then_pivot = [e for e in arr if e < pivot]
        equal_to_pivot = [e for e in arr if e == pivot]
        greater_then_pivot = [e for e in arr if e > pivot]

        return QuickSort(less_then_pivot) + equal_to_pivot + QuickSort(greater_then_pivot)

arr = [3, 4, 1, 3, 7, 5]
arr2 = QuickSort(arr)

print(arr2)