def LinearSearch(arr, data):
    for i in range(len(arr)) :
        if arr[i] == data:
            return i;

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

search = LinearSearch(arr, 4)

print(search)