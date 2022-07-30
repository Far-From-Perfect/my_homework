from collections import deque


def result(arr, size):
    queue = deque()
    idx = 0
    res = []
    ans = [0] * len(arr)
    while len(arr) > 0:
        if len(queue) < size:
            tmp = arr.popleft()
            tmp.append(idx)
            idx += 1
            if len(queue) > 0 and queue[-1][0] + queue[-1][1] > tmp[0]:
                tmp[0] = queue[-1][0] + queue[-1][1]
                queue.append(tmp)
            else:
                queue.append(tmp)
        elif queue[0][0] + queue[0][1] <= arr[0][0]:
            tmp = arr.popleft()
            tmp.append(idx)
            idx += 1
            if tmp[0] > queue[-1][0] + queue[-1][1]:
                queue.append(tmp)
            else:
                tmp[0] = queue[-1][0] + queue[-1][1]
                queue.append(tmp)
            res.append(queue.popleft())
        else:
            arr.popleft()
            res.append([-1, idx])
            idx += 1
    while len(queue) > 0:
        res.append(queue.popleft())
    for i in res:
        ans[i[-1]] = i[0]
    return ans


size, n = map(int, input().split())
buffer = deque()
for i in range(n):
    arrival, duration = map(int, input().split())
    buffer.append([arrival, duration])
if n == 0:
    pass
else:
    res = result(buffer, size)
    for i in res:
        print(i)