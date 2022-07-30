def search(arr, low, high, key):
    if high < low:
        return -2
    middle = low + (high - low) // 2
    if key == arr[middle]:
        return middle
    elif key < arr[middle]:
        return search(arr, low, middle-1, key)
    else:
        return search(arr, middle+1, high, key)


n, *arr_1 = map(int, input().split())
k, *arr_2 = map(int, input().split())

for i in arr_2:
    print(search(arr_1, 0, len(arr_1)-1, i)+1, end=' ')