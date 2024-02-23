def BinarySearch(arr, data):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == data:
            return mid

        elif arr[mid] < data:
            low = mid + 1

        else:
            high = mid - 1
    
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = BinarySearch(arr, 0)

print(s)