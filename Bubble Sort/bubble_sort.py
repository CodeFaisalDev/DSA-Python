def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
arr = [5, 7, 4, 1, 8, 3, 0]

BubbleSort(arr)

print(arr)