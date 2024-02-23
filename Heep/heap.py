def heapify(arr, size, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def insert(arr, data):
    size = len(arr)

    if size == 0:
        arr.append(data)
    else:
        arr.append(data)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size, i)

def delete(arr, data):
    size = len(arr)
    i = 0
    for i in range(0, size):
        if data == arr[i]:
            break
    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(data)

    size = len(arr)
    for i in range((size // 2) - 1, -1, -1):
        heapify(arr, size, i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max Heap array: " + str(arr))
delete(arr, 4)
print("After deleting an element: " + str(arr))
