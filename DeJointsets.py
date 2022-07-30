class Table:
    def __init__(self, lst) -> None:
        self.parent = [i for i in range(len(lst))]
        self.rank = [0] * len(lst)
        self.vals = lst
        self.max = max(lst)

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return self.max
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.vals[i_id] += self.vals[j_id]
        else:
            self.parent[i_id] = j_id
            self.vals[j_id] += self.vals[i_id]
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        self.max = max(self.max, self.vals[i_id], self.vals[j_id])
        return self.max

n, m = map(int, input().split())
size = [int(x) for x in input().split()]
# size = [Node(size[i], i) for i in range(len(size))]
table = Table(size)
for i in range(m):
    num1, num2 = map(int, input().split())
    print(table.union(num1-1, num2-1))

class DeJointSet:
    def __init__(self, num) -> None:
        self.parent = [i for i in range(num)]

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        self.parent[j_id] = i_id
        

n, e, d = map(int, input().split())
dejointset = DeJointSet(n)
for un in range(e):
    num1, num2 = map(int, input().split())
    dejointset.union(num1-1, num2-1)

flag = 1
for de in range(d):
    num1, num2 = map(int, input().split())
    if dejointset.find(num1-1) == dejointset.find(num2-1):
        flag = 0
        break
print(flag)