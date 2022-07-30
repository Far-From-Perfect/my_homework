def calc(num):
    F = [0] + [num+1 for _ in range(num-1)]
    prev = [0 for _ in range(num)]

    for i in range(1, num+1):
        for j in (i*2, i*3, i+1):
            if j - 1 < num and F[i-1] + 1 < F[j-1]:
                F[j-1] = F[i-1] + 1
                prev[j-1] = i
    return F, prev


n = int(input())
f, prev = calc(n)
res = [n]
while n > 1:
    res.append(prev[n-1])
    n = prev[n-1]

print(f[-1])
print(*reversed(res))