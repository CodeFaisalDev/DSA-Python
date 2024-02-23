def heapify(arr, size, i):
    largest = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    if leftChild < size and arr[leftChild] > arr[largest]:
        largest = leftChild
    if rightChild < size and arr[rightChild] > arr[largest]:
        largest = rightChild
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def heapSort(arr):
    size = len(arr)

    for i in range((size // 2) - 1, -1, -1):
        heapify(arr, size, i)
    
    for i in range((size - 1), 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 5, 4, 7, 9, 1]

heapSort(arr)

for i in range(len(arr)):
    print(arr[i])
