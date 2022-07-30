from collections import deque


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = []

    def upd(self, x):
        self.child.append(x)


def bfs(root):
    if len(root.child) == 0:
        return 1
    q = deque()
    for elem in root.child:
        q.append(elem)
    level = 0
    while True:
        len_queue = len(q)

        while len_queue != 0:
            buffer = q.copy()
            q = deque()

            for child in buffer:
                if child.child:
                    for elem in child.child:
                        q.append(elem)

            len_queue = 0
            level += 1
        if len(q) == 0:
            return level+1


n, arr = int(input()), [int(x) for x in input().split()]
res = [Node(x) for x in range(n)]
for i, elem in enumerate(res):
    if arr[i] == -1:
        elem.parent = -1
        root = elem
    else:
        elem.parent = arr[i]
        res[arr[i]].upd(elem)
print(bfs(root))