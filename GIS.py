def res(F, prev, inf):
    F = len(list(filter(lambda x: x if abs(x) != inf else None, F)))
    c = F
    result = []
    for i in reversed(prev):
        if i[0] == c:
            result.append(i[1]+1)
            c -= 1
    return F, reversed(result)


def gis(A: list):
    inf = 10 ** 10
    F = [-inf] * (len(A)+1)
    F[0] = inf
    prev = []
    for i in range(len(A)):
        left = 0
        right = len(A)
        while right - left > 1:
            mid = (right + left) // 2
            if F[mid] < A[i]:
                right = mid
            else:
                left = mid
        F[right] = A[i]
        prev.append([right, i, A[i]])
    return res(F, prev, inf)


n = int(input())
lst = [int(x) for x in input().split()]
F, result = gis(lst)
print(F)
print(*result)
