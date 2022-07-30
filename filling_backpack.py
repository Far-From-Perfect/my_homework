n, w = [int(x) for x in input().split()]
lst = [[int(x) for x in input().split()] for i in range(n)]

for i in lst:
    i.append(i[0]/i[1])
lst.sort(key= lambda x: x[-1])
res = 0
while w > 0 and len(lst) > 0:
    price, weight, pw = lst.pop()
    if w >= weight:
        res += price
        w -= weight
    else:
        res += (weight - (weight - w)) * pw
        w -= weight


print(f'{res:.3f}')


def backpack(A: list, W: int):
    """Динамическое программирование; заполнение рюкзака неповторяющимеся значениями"""
    F = [[0 for j in range(W+1)] for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, W+1):
            if A[i-1] <= j:
                F[i][j] = max(F[i-1][j], A[i-1] + F[i-1][j-A[i-1]])
            else:
                F[i][j] = F[i-1][j]
    return F[len(A)][W]


W, n = map(int, input().split())
lst = [int(x) for x in input().split()]
print(backpack(lst, W))
