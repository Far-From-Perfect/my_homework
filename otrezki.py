n = int(input())
lst = [[int(x) for x in input().split()] for i in range(n)]
lst.sort(key=lambda k: k[1])
r = lst[0][1]
ans = [r]
for i, arr in enumerate(lst[1:]):
    if r < arr[0]:
        r = arr[1]
        ans.append(r)

print(len(ans))
print(*ans)