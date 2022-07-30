def search(arr, x, l=0, r=-1):
    if x > arr[-1] or x < arr[0]:
        return -2
    if x >= arr[len(arr)//2]:
        if x == arr[len(arr)//2]:
            return l + len(arr) // 2
        l += len(arr) // 2
        return search(arr[len(arr)//2:], x, l, r)
    if x < arr[len(arr)//2]:
        r -= len(arr) // 2
        return search(arr[:len(arr)//2], x, l, r)


n, *arr_1 = map(int, input().split())
k, *arr_2 = map(int, input().split())

for i in arr_2:
    print(search(arr_1, i)+1, end=' ')