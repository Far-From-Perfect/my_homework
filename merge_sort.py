class Cnt:
    def __init__(self, num):
        self.num = num

    def upd(self, lenght, idx):
        self.num += lenght - idx


def merge(A: list, B: list):
    C = [0] * (len(A) + len(B))
    i, k, n = 0, 0, 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            cnt.upd(len(A), i)
            k += 1
        n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C


def merge_sort(arr):
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    arr[:] = C[:]


a = int(input())
arr = [int(x) for x in input().split()]
cnt = Cnt(0)
merge_sort(arr)
print(cnt.num)
